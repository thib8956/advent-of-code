#! /usr/bin/env python3
from collections import defaultdict
from enum import Enum
import logging
import os

loglevel = (os.getenv("LOGLEVEL") or "WARN").upper()
logging.basicConfig(format="%(levelname)s:%(message)s", level=loglevel)


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
    BASE = 9
    TERMINATION = 99


class Mode(Enum):
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2


class Instruction:
    def __init__(self, memory, ip, base):
        self.ip = ip
        self.memory = memory
        self.opcode = memory[ip]
        # A B C D E
        # 0 1 1 0 3 
        # A B C modes, DE opcode
        self.operation = Operation(self.opcode % 100)
        self.modes = [Mode(get_nth_digit(n, self.opcode)) for n in range(2, 5)]
        self.handler_name = f"handle_{self.operation.name.lower()}"
        self.handler = getattr(self, self.handler_name, self.handle_unknown)
        self.input = None
        self.output = None
        self.halted = False
        self.base = base

    def __repr__(self):
        return f"[{self.opcode}] Instruction({self.operation}, {self.modes})"

    def handle(self):
        return self.handler()

    def handle_addition(self):
        first, second = self._get_parameters()
        logging.debug(f"ADD {first} {second}")
        result = first + second
        address = self._get_write_addr(3)
        logging.debug(f"{address}")
        self._write(address, result)
        self.ip += 4
        return self.ip

    def handle_multiplication(self):
        first, second = self._get_parameters()
        logging.debug(f"MUL {first} {second}")
        result = first * second
        address = self._get_write_addr(3)
        self._write(address, result)
        self.ip += 4
        return self.ip

    def handle_input(self):
        address = self._get_write_addr(1)
        self._write(address, self.input)
        logging.debug(f"INP {address} {self.input}")
        self.ip += 2
        return self.ip

    def handle_output(self):
        self.output = self._get_value(1)
        logging.debug(f"OUT {self.output}")
        self.ip += 2
        return self.ip

    def handle_jmp_if_true(self):
        first, second = self._get_parameters()
        logging.debug(f"JMPT {first} {second} {first != 0}")
        return second if first != 0 else self.ip + 3

    def handle_jmp_if_false(self):
        first, second = self._get_parameters()
        logging.debug(f"JMPF {first} {second}")
        return second if first == 0 else self.ip + 3

    def handle_less_than(self):
        first, second = self._get_parameters()
        logging.debug(f"LT {first} {second} {first < second}")
        address = self._get_write_addr(3)
        self._write(address, int(first < second))
        self.ip += 4
        return self.ip

    def handle_equals(self):
        first, second = self._get_parameters()
        logging.debug(f"EQ {first} {second}")
        address = self._get_write_addr(3)
        self._write(address, int(first == second))
        self.ip += 4
        return self.ip

    def handle_termination(self):
        logging.debug("HALT")
        self.halted = True
        return self.ip

    def handle_base(self):
        self.base += self._get_value(1)
        logging.debug(f"BASE {self.base}")
        self.ip += 2
        return self.ip

    def handle_unknown(self):
        raise ValueError(f"Unknown operation <{self.operation}> @ [{self.ip}]")

    def _get_value(self, offset):
        value = self.memory[self.ip + offset]
        match self.modes[offset - 1]:
            case Mode.POSITION: return self.memory[value] if value < len(self.memory) else 0
            case Mode.IMMEDIATE: return value
            case Mode.RELATIVE: return self.memory[value + self.base]
            case _: raise ValueError(f"{self.modes[i]}")

    def _get_write_addr(self, offset):
        value = self.memory[self.ip + offset]
        match self.modes[offset - 1]:
            case Mode.POSITION: return value
            case Mode.RELATIVE: return value + self.base
            case _: raise ValueError(f"{self.modes[i]}")

    def _get_parameters(self):
        first = self._get_value(1)
        second = self._get_value(2)
        return first, second
    
    def _write(self, address, value):
        while address >= len(self.memory):
            self.memory += [0] * len(self.memory)
        self.memory[address] = value


class Interpreter:
    def __init__(self, program, stdin=[]):
        self.ip = 0
        self.stdin = stdin
        self.stdout = []
        self.memory = program[::]
        self.halted = False
        self.base = 0

    def __repr__(self):
        return f"Interpreter(ip={self.ip}, stdin={self.stdin}, stdout={self.stdout}, halted={self.halted})"

    def interpret(self, break_on_input=False, break_on_output=True):
        while not self.halted:
            # fetch next instruction
            instruction = Instruction(self.memory, self.ip, self.base)
            # pause if INP + break on input
            if instruction.operation == Operation.INPUT:
                if break_on_input and self.stdin == []:
                    break
                else:
                    instruction.input = self.stdin.pop(0)
            # execute instruction
            self.ip = instruction.handle()
            self.base = instruction.base
            logging.debug(f"IP {self.ip}")
            if instruction.output is not None:
                self.stdout.append(instruction.output)
                if break_on_output:
                    break
            if instruction.halted:
                self.halted = True


def interpret_intcode(program, stdin=[]):
    interpreter = Interpreter(program, stdin)
    interpreter.interpret(break_on_output=False)
    return interpreter

