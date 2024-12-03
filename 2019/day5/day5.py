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
        ip += 2
        program[program[ip + 1]] = int(input("Enter ID > "))
        return ip

    def handle_output(self, program, ip):
        print("OUT ", program[program[ip + 1]])
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


def interpret_intcode(program, stdin=None):
    ip = 0
    while program[ip] != 99:
        opcode = program[ip]
        instruction = Instruction(opcode)
        ip = instruction.handle(program, ip)


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
    print("\nAll tests passed.\n")


def run_input_program(filename):
    import os

    SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(SCRIPT_DIR, filename)) as inp:
        print("Start of input program.")
        memory = [int(x) for x in inp.readline().strip().split(",")]
        interpret_intcode(memory, 5)


if __name__ == "__main__":
    tests()
    # a = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
    # b = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]

    # interpret_intcode(b, 0)
    # interpret_intcode(a, 0)
    run_input_program("input.txt")
