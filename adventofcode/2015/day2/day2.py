#!/usr/bin/env python3
from functools import reduce
from operator import mul


def part1(inp):
    total = 0
    for line in inp:
        l, w, h = map(int, line.split("x"))
        faces = [l * w, w * h, h * l]
        total += sum(2 * x for x in faces) + min(faces)
    print("Part 1: ", total)


def part2(inp):
    total = 0
    for line in inp:
        line = list(map(int, line.split("x")))
        total += sum(sorted(line)[:2]) * 2 + reduce(mul, line, 1)
    print("Part 2:", total)


if __name__ == "__main__":
    import fileinput

    lines = [x.rstrip() for x in fileinput.input()]
    part1(lines)
    part2(lines)
