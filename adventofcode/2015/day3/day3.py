#!/usr/bin/env python3
import fileinput
from itertools import zip_longest


def grouper(n, iterable):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args)


def move(c, x, y):
    if c == "^":
        y += 1
    elif c == ">":
        x += 1
    elif c == "v":
        y -= 1
    elif c == "<":
        x -= 1
    return x, y


def part1(inp):
    x, y = 0, 0
    visited = {(x, y)}
    for c in inp:
        x, y = move(c, x, y)
        visited.add((x, y))
    print("Part 1: ", len(visited))


def part2(inp):
    x1, y1 = 0, 0
    x2, y2 = 0, 0
    visited = {(x1, y1)}
    for move1, move2 in grouper(2, inp):
        x1, y1 = move(move1, x1, y1)
        x2, y2 = move(move2, x2, y2)
        visited.add((x1, y1))
        visited.add((x2, y2))
    print("Part 2: ", len(visited))


def main(inp):
    part1(inp)
    part2(inp)


if __name__ == "__main__":
    inp = next(x.rstrip() for x in fileinput.input())
    main(inp)
