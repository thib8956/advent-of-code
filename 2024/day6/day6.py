from itertools import cycle
from dataclasses import dataclass
from pprint import pprint


@dataclass(frozen=True)
class Vec2d:
    x: int
    y: int

    def __add__(self, other): 
        return Vec2d(self.x + other.x, self.y + other.y)


DIRECTIONS = (
    Vec2d(0, -1),   # N
    Vec2d(1, 0),    # E
    Vec2d(0, 1),    # S
    Vec2d(-1, 0),   # W
)


def find_start_pos(grid):
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == "^":
                return Vec2d(x, y)
    raise RuntimeError("No start position found")


def find_path(grid, pos):
    directions = cycle(DIRECTIONS)
    direction = next(directions)
    path = {(pos, direction)}
    while True:
        new_pos = pos + direction
        if 0 <= new_pos.y < len(grid) and 0 <= new_pos.x < len(grid[0]):
            while grid[new_pos.y][new_pos.x] == "#":
                direction = next(directions)
                new_pos = pos + direction

            pos = new_pos
            if (pos, direction) in path:  # if we visited this position while going the same direction, we are in a loop
                visited = [x for x, _ in path]
                return visited, True
            path.add((pos, direction))
        else:
            visited = [x for x, _ in path]
            return visited, False
    raise RuntimeError("Should not happen")


def main(grid):
    pos = find_start_pos(grid)

    path, _ = find_path(grid, pos)
    print("Part 1: ", len(set(path)))

    loops = []
    last_obstacle_pos = None
    for obstacle_pos in path: 
        if pos == obstacle_pos:
            continue

        grid[obstacle_pos.y][obstacle_pos.x] = "#"
        path, is_loop = find_path(grid, pos)
        if is_loop:
            loops.append(obstacle_pos)
        grid[obstacle_pos.y][obstacle_pos.x] = "."
    print("Part 2: ", len(set(loops)))



if __name__ == "__main__":
    import sys
    infile = sys.argv[1] if 1 < len(sys.argv) else "example.txt"
    with open(infile) as f:
        grid = [list(l.rstrip()) for l in f.readlines()]
        main(grid)

