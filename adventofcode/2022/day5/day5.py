#!/usr/bin/env python3
import fileinput
import re
from collections import defaultdict


def parse_data(data):
    stacks, commands = defaultdict(list), []
    parsing_stacks = True
    for line in data:
        if line == "":
            parsing_stacks = False
            continue
        if parsing_stacks:
            for i, c in enumerate(line):
                if c.isalpha():
                    stacks[i].append(c)
        else:
            commands.append(tuple(int(x) for x in re.findall(r"\d+", line)))

    stacks = [v[::-1] for k, v in sorted(stacks.items())]
    return stacks, commands


def part1(stacks, commands):
    for qty, src, dst in commands:
        for _ in range(qty):
            x = stacks[src - 1].pop()
            stacks[dst - 1].append(x)
    return "".join(s[-1] for s in stacks)


def part2(stacks, commands):
    for qty, src, dst in commands:
        stacks[dst - 1] += stacks[src - 1][-qty:]
        stacks[src - 1] = stacks[src - 1][:-qty]
    return "".join(s[-1] for s in stacks)


def main(data):
    stacks, commands = parse_data(data)
    print("Part 1: ", part1([s[:] for s in stacks], commands))
    print("Part 2: ", part2([s[:] for s in stacks], commands))


if __name__ == "__main__":
    with fileinput.input() as f:
        data = [x.rstrip() for x in f]
    main(data)
