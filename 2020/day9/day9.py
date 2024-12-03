#!/usr/bin/env python3
import itertools


def part1(inp):
    preamble_size = 25
    with open(inp) as infile:
        cleanfile = (int(l.rstrip()) for l in infile)
        for nums in window(cleanfile, preamble_size + 1):
            candidate = nums[-1]
            if not test_number(candidate, nums[:-1]):
                return candidate
    return -1


def window(seq, n):
    it = iter(seq)
    result = tuple(itertools.islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result


def test_number(num, previous):
    sums = set(sum(x) for x in itertools.combinations(previous, 2))
    return num in sums


def part2(infile, target: int):
    lines = [int(l.rstrip()) for l in open(infile).readlines()]
    total = 0
    visited = []
    for index, _ in enumerate(lines):
        i = index
        while total < target:
            total += lines[i]
            visited.append(lines[i])
            i += 1
            if total == target:
                return max(visited) + min(visited)
        visited.clear()
        total = 0


if __name__ == "__main__":
    invalid_number = part1("input.txt")
    print("part1 ", invalid_number)
    print("part2 ", part2("input.txt", invalid_number))
