#!/usr/bin/env python3
from rules import part1_rules


def main(grid, rules):
    generation = 0
    while True:
        changes, next_grid = step(grid, rules)
        generation += 1
        grid = next_grid
        assert generation < 1000
        if changes == 0:
            return next_grid.count("#")


def step(grid, rules):
    changes = 0
    next_grid = grid[:]
    for index, cell in enumerate(grid):
        try:
            changes += rules[cell](index, grid, next_grid)
        except KeyError:
            pass
    return changes, next_grid


if __name__ == "__main__":
    with open("input.txt") as infile:
        grid = list("".join(infile.read().splitlines()))
        print("Part 1 ", main(grid, rules=part1_rules))

    # print("Part 2 ", main(grid, rules={"L": handle_empty_2, "#": handle_occupied_2}))
