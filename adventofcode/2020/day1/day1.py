#! /usr/bin/env python3
from itertools import product


def part1(inp):
    inp = [int(x) for x in inp]
    result_pairs = [x for x in list(product(inp, inp)) if sum(x) == 2020]
    print(result_pairs)
    print(result_pairs[0][0] * result_pairs[0][1])


def part2(inp):
    inp = [int(x) for x in inp]
    result_pairs = [x for x in list(product(inp, repeat=3)) if sum(x) == 2020]
    print(result_pairs)
    print(result_pairs[0][0] * result_pairs[0][1] * result_pairs[0][2])


if __name__ == "__main__":
    import fileinput
    lines = [x for x in fileinput.input()]
    part1(lines)
    part2(lines)

