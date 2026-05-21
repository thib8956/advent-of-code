#!/usr/bin/env python3
import fileinput
import re
from functools import reduce
from operator import mul


def calc(stack, operator):
    if operator == "+":
        return sum(int(x) for x in stack)
    elif operator == "*":
        return reduce(mul, map(int, stack))
    else:
        raise NotImplementedError(operator)


def part1(inp):
    lines = [re.split(r"\s+", x.strip()) for x in inp]
    total = 0
    for col in zip(*lines):
        operands, operator = col[:-1], col[-1]
        result = calc([int(x) for x in operands], operator)
        total += result
    print("Part 1: ", total)


def part2(lines):
    total = 0
    max_len = max(len(x) for x in lines)
    numbers = []
    operator = None
    for i in range(max_len - 1, -1, -1):
        digits = []
        for line in lines:
            if i >= len(line):
                continue
            ch = line[i]
            if ch in "*+":
                operator = ch
                break
            elif ch != " ":
                digits.append(ch)

        if digits:
            numbers.append(int("".join(digits)))

        if operator is not None:
            total += calc(numbers, operator)
            numbers = []
            operator = None

    print("Part 2: ", total)


if __name__ == "__main__":
    lines = [x.rstrip() for x in fileinput.input()]
    part1(lines)
    part2(lines)
