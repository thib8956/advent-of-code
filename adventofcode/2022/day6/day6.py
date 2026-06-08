#!/usr/bin/env python3
import fileinput


def main(inp):
    result = 0
    for i, _ in enumerate(inp):
        if i < 3:
            continue
        if len(set(line[i - 3 : i + 1])) == 4:  # first 4 consecutive unique characters
            result = i + 1
            break
    print("Part 1: ", result)

    for i, _ in enumerate(inp):
        if i < 13:
            continue
        # first 14 consecutive unique characters
        if len(set(line[i - 13 : i + 1])) == 14:
            result = i + 1
            break
    print("Part 2: ", result)


if __name__ == "__main__":
    with fileinput.input() as f:
        line = next(x.rstrip() for x in fileinput.input())
    main(line)
