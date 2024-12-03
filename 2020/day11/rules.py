#!/usr/bin/env python3
from itertools import count, takewhile

directions = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
)

grid_width = 98
grid_height = 97


def handle_empty(index, grid, next_grid):
    """
    If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    """
    neighbors = count_neighbors(index, grid)
    if neighbors == 0:
        next_grid[index] = "#"
        return 1
    return 0


def handle_occupied(index, grid, next_grid):
    """
    If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    """
    neighbors = count_neighbors(index, grid)
    if neighbors >= 4:
        next_grid[index] = "L"
        return 1
    return 0


def count_neighbors(pos, grid):
    neighbors = 0
    x = pos % grid_width
    y = pos // grid_width
    for (dx, dy) in directions:
        xx = x + dx
        yy = y + dy
        if not in_bounds((xx, yy)):
            continue

        if grid[yy * grid_width + xx] == "#":
            neighbors += 1
    return neighbors


def handle_empty_2(index, grid, next_grid):
    """
    If a seat is empty and there are no occupied seat visible in neither direction,
    the seat becomes occupied
    """
    neighbors = 0
    x = index % grid_width
    y = index // grid_width
    for direction in directions:
        # keep moving in the specified direction, while checking
        # that we are in bounds of the grid
        for xx, yy in takewhile(in_bounds, move(x, y, direction)):
            cell = grid[yy * grid_width + xx]
            if cell == "#":
                neighbors += 1
            elif cell == "L":
                break  # No occupied seat in that direction, we can break

    if neighbors == 0:
        next_grid[index] = "#"
        return 1
    return 0


def handle_occupied_2(index, grid, next_grid):
    """
    An occupied seat becomes empty if there are five or more visible occupied
    seats in either direction.
    """
    occupied = 0
    x = index % grid_width
    y = index // grid_width
    for direction in directions:
        for xx, yy in takewhile(in_bounds, move(x, y, direction)):
            print(xx, yy)
            cell = grid[yy * grid_width + xx]

            if cell == "#":
                occupied += 1

    if occupied >= 5:
        next_grid[index] = "L"
        return 1
    return 0


def in_bounds(pos):
    x, y = pos
    return 0 <= x < grid_width and 0 <= y < grid_height


def move(x, y, direction):
    pos = x, y
    while True:
        yield pos
        pos = x + direction[0], y + direction[1]


part1_rules = {"L": handle_empty, "#": handle_occupied}
part2_rules = {"L": handle_empty_2, "#": handle_occupied_2}
