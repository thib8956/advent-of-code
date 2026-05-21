#!/usr/bin/env python3
import fileinput


def part1(inp):
    "Simple brute force solution"
    total = 0
    for line in inp:
        max_jolt = 0
        for i, a in enumerate(line):
            for b in line[i + 1 :]:
                max_jolt = max(max_jolt, int(a + b))
        total += max_jolt
    print("Part 1:", total)


def find_max_joltage(inp):
    """
    Greedy algorithm: pick 12 digits from the input to form the largest
    possible number, keeping the original order.
    """
    stack = []
    for i, current in enumerate(inp):
        while stack != [] and current > stack[-1]:
            remaining_len = len(inp) - i
            if len(stack) + remaining_len <= 12:
                break
            stack.pop()
        stack.append(current)
    return "".join(stack[:12])


def part2(inp):
    total = 0
    for line in inp:
        res = find_max_joltage(line)
        total += int(res)
    print("Part 2:", total)


def main(inp):
    part1(inp)
    part2(inp)


if __name__ == "__main__":
    lines = [x.rstrip() for x in fileinput.input()]
    main(lines)
