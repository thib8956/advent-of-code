#!/usr/bin/env python3
import fileinput
from collections import deque

DIRECTIONS = [
    0 - 1j,  # NORTH
    1 - 1j,  # NORTHEAST
    1 + 0j,  # EAST
    1 + 1j,  # SOUTHEAST
    0 + 1j,  # SOUTH
    -1 + 1j,  # SOUTHWEST
    -1 + 0j,  # WEST
    -1 - 1j,  # NORTHWEST
]


def parse_grid(lines):
    grid = set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "@":
                grid.add(complex(x, y))
    return grid


def can_be_accessed(roll, grid):
    """
    The forklifts can only access a roll of paper if there are fewer than four
    rolls of paper in the eight adjacent positions.
    """
    total = sum(1 for direction in DIRECTIONS if roll + direction in grid)
    return total < 4


def main(inp):
    # Part 1
    grid = parse_grid(inp)
    total = 0
    total = sum(1 for roll in grid if can_be_accessed(roll, grid))
    print(f"Part 1: {total}")

    # Part 2
    total = 0
    # use a queue to avoid rechecking all rolls each iteration
    # we only check rolls that are adjacent to a roll that was removed
    accessible_queue = deque(roll for roll in grid if can_be_accessed(roll, grid))
    while accessible_queue:
        roll = accessible_queue.popleft()
        if roll not in grid:
            continue  # roll was already removed

        total += 1
        grid.remove(roll)
        # check if new rolls are accessible
        for direction in DIRECTIONS:
            neighbor = roll + direction
            if neighbor in grid and can_be_accessed(neighbor, grid):
                accessible_queue.append(neighbor)
    print(f"Part 2: {total}")


if __name__ == "__main__":
    lines = [x.rstrip() for x in fileinput.input()]
    main(lines)
