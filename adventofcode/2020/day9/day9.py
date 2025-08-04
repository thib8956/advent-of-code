#!/usr/bin/env python3
import itertools


def part1(lines):
    preamble_size = 25
    for nums in window(lines, preamble_size + 1):
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


def part2(lines, target: int):
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


def main(f):
    lines = [int(l.rstrip()) for l in f]
    invalid_number = part1(lines)
    print("part1 ", invalid_number)
    print("part2 ", part2(lines, invalid_number))


if __name__ == "__main__":
    import fileinput
    main(fileinput.input())

