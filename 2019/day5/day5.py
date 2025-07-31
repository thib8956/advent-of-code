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
        self.operation = Operation(opcode % 100)
        self.modes = [Mode(get_nth_digit(n, opcode)) for n in range(2, 5)]
        self.handler_name = f"handle_{self.operation.name.lower()}"
        self.handler = getattr(self, self.handler_name, self.handle_termination)
        self.input = 0
        self.output = 0

    def __repr__(self):
        return f"Instruction({self.operation}, {self.modes})"

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
        param = (
            program[ip + 1]
            if self.modes[0] is Mode.IMMEDIATE
            else program[program[ip + 1]]
        )

        self.output = param
        print("OUT ", param)
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
        print("HALT")
        return ip

    def _get_parameters(self, program, ip):
        first = (
            program[ip + 1]
            if self.modes[0] is Mode.IMMEDIATE
            else program[program[ip + 1]]
        )
        second = (
            program[ip + 2]
            if self.modes[1] is Mode.IMMEDIATE
            else program[program[ip + 2]]
        )
        return first, second


def interpret_intcode(program, stdin=[]):
    ip = 0
    while program[ip] != 99:
        opcode = program[ip]
        instruction = Instruction(opcode)
        if instruction.operation == Operation.INPUT:
            instruction.input=stdin.pop(0)
        ip = instruction.handle(program, ip)
    return instruction.output


def tests():
    inputs = (
        [1, 0, 0, 0, 99],  # ADD 1 + 1 to location 0
        [2, 3, 0, 3, 99],  # MUL 2 * 3 to location 3
        [2, 4, 4, 5, 99, 0],
        [1, 1, 1, 4, 99, 5, 6, 0, 99],
        [1101, 1, 1, 0, 99],  # ADD 1 + 1 to location 0 (direct access)
    )
    expected_outputs = (
        [2, 0, 0, 0, 99],  # 1 + 1 = 2
        [2, 3, 0, 6, 99],  # 3 * 2 = 6
        [2, 4, 4, 5, 99, 9801],  # 99 * 99 = 9801
        [30, 1, 1, 4, 2, 5, 6, 0, 99],
        [2, 1, 1, 0, 99],  # 1 + 1 = 2 (direct access)
    )
    for i, inp in enumerate(inputs):
        result = inp[:]
        interpret_intcode(result)
        assert (
            result == expected_outputs[i]
        ), f"Expected output for {inp} is {expected_outputs[i]}, but found {result} instead."

    # factorial test
    fac = [3,29,1007,29,2,28,1005,28,24,2,27,29,27,1001,29,-1,29,1101,0,0,28,1006,28,2,4,27,99,1,0,0]
    res = interpret_intcode(fac, [4]) 
    assert res == 24, f"Expected 24 but got {res}"

    print("\nAll tests passed.\n")


def run_input_program(inp):
    print("Start of input program.")
    memory = [int(x) for x in inp.readline().strip().split(",")]
    part1 = interpret_intcode(memory[::], [1]) 
    print("Part 1: ", part1)
    part2 = interpret_intcode(memory[::], [5])
    print("Part 2: ", part2)


if __name__ == "__main__":
    tests()
    import fileinput
    run_input_program(fileinput.input())

