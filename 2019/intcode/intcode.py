#! /usr/bin/env python3
from collections import namedtuple
from enum import Enum
import logging

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.WARN)


def get_nth_digit(n, number):
    "Returns the nth digit of the input number"
    return number // 10 ** n % 10


class Operation(Enum):
    ADDITION = 1
    MULTIPLICATION = 2
    INPUT = 3
    OUTPUT = 4
    JMP_IF_TRUE = 5
    JMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    TERMINATION = 99


class Mode(Enum):
    POSITION = 0
    IMMEDIATE = 1


class Instruction:
    def __init__(self, opcode):
        self.opcode = opcode
        # A B C D E
        # 0 1 1 0 3 
        # A B C modes, DE opcode
        self.operation = Operation(opcode % 100)
        self.modes = [Mode(get_nth_digit(n, opcode)) for n in range(2, 5)]
        self.handler_name = f"handle_{self.operation.name.lower()}"
        self.handler = getattr(self, self.handler_name, self.handle_termination)
        self.input = None
        self.output = None
        self.halted = False

    def __repr__(self):
        return f"[{self.opcode}] Instruction({self.operation}, {self.modes})"

    def handle(self, program, ip):
        return self.handler(program, ip)

    def handle_addition(self, program, ip):
        first, second = self._get_parameters(program, ip)
        logging.debug(f"ADD {first} {second}")
        result = first + second
        # the last mode should *always* be POSITION
        program[program[ip + 3]] = result
        ip += 4
        return ip

    def handle_multiplication(self, program, ip):
        first, second = self._get_parameters(program, ip)
        logging.debug(f"MUL {first} {second}")
        result = first * second
        # the last mode should *always* be POSITION
        program[program[ip + 3]] = result
        ip += 4
        return ip

    def handle_input(self, program, ip):
        program[program[ip + 1]] = self.input
        ip += 2
        return ip

    def handle_output(self, program, ip):
        self.output = self._get_param(program, ip)
        logging.debug(f"OUT {self.output}")
        ip += 2
        return ip

    def handle_jmp_if_true(self, program, ip):
        first, second = self._get_parameters(program, ip)
        logging.debug(f"JMPT {first} {second}")
        return second if first != 0 else ip + 3

    def handle_jmp_if_false(self, program, ip):
        first, second = self._get_parameters(program, ip)
        logging.debug(f"JMPF {first} {second}")
        return second if first == 0 else ip + 3

    def handle_less_than(self, program, ip):
        first, second = self._get_parameters(program, ip)
        logging.debug(f"LT {first} {second}")
        program[program[ip + 3]] = int(first < second)
        ip += 4
        return ip

    def handle_equals(self, program, ip):
        first, second = self._get_parameters(program, ip)
        logging.debug(f"EQ {first} {second}")
        program[program[ip + 3]] = int(first == second)
        ip += 4
        return ip

    def handle_termination(self, program, ip):
        logging.debug("HALT")
        self.halted = True
        return ip

    def _get_param(self, program, ip, i=0):
        return (
            program[ip + i + 1]
            if self.modes[i] is Mode.IMMEDIATE
            else program[program[ip + i + 1]]
        )

    def _get_parameters(self, program, ip):
        first = self._get_param(program, ip, 0)
        second = self._get_param(program, ip, 1)
        return first, second


class Interpreter:
    def __init__(self, program, stdin=[]):
        self.ip = 0
        self.stdin = stdin
        self.stdout = []
        self.program = program
        self.halted = False

    def __repr__(self):
        return f"Interpreter(ip={self.ip}, {self.stdin}, {self.stdout}, {self.halted})"

    def next_instruction(self):
        instruction = Instruction(self.program[self.ip])
        if instruction.operation == Operation.INPUT:
            instruction.input = self.stdin.pop(0)
        self.ip = instruction.handle(self.program, self.ip)
        if instruction.output is not None:
            self.stdout.append(instruction.output)
        elif instruction.halted:
            self.halted = True
        return instruction

    def interpret(self, break_on_output=True):
        while instruction := self.next_instruction():
            if self.halted:
                break
            if break_on_output and instruction.output is not None:
                break


def interpret_intcode(program, stdin=[]):
    interpreter = Interpreter(program, stdin)
    interpreter.interpret(break_on_output=False)
    return interpreter.stdout

