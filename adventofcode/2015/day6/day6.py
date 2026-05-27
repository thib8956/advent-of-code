#!/usr/bin/env python3
import fileinput
import re


def part1(inp):
    """
    Part 1: simple brute force solution. Use a 1D array to represent the grid.
    Use sice operations whenever possible because they are faster than iterating.
    """
    grid = [False] * 1000 * 1000
    for line in inp:
        x1, y1, x2, y2 = map(int, re.findall(r"(\d+)", line))
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        for y in range(y1, y2 + 1):
            start = y * 1000 + x1
            end = y * 1000 + x2 + 1
            # assigning to the slice is faster than iterating
            if line.startswith("turn on"):
                grid[start:end] = [True] * (end - start)
            elif line.startswith("turn off"):
                grid[start:end] = [False] * (end - start)
            elif line.startswith("toggle"):
                for i in range(start, end):
                    grid[i] = not grid[i]
    return sum(grid)


def main(inp):
    print("Part 1: ", part1(inp))


if __name__ == "__main__":
    lines = [x.rstrip() for x in fileinput.input()]
    main(lines)
