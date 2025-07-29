#!/usr/bin/env python3
from collections import Counter


def part1(adapters):
    counts = Counter()
    # 1 for the socket, of 3 for the device
    for current, next in zip([0] + adapters, adapters + [3]):
        counts[next - current] += 1
    return counts[1] * counts[3]


def part2(adapters):
    counts = Counter({0: 1})
    for jolt in adapters:
        s = counts[jolt - 1] + counts[jolt - 2] + counts[jolt - 3]
        counts[jolt] = s
    return max(counts.values())


def main(f):
    adapters = sorted(int(l.rstrip()) for l in f)
    print(part1(adapters))
    print(part2(adapters))


if __name__ == "__main__":
    import fileinput
    main(fileinput.input())

