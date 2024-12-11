from dataclasses import dataclass


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


def in_bounds(grid, pos):
    return 0 <= pos.y < len(grid) and 0 <= pos.x < len(grid[0])


def get_pos(grid, pos):
    return grid[pos.y][pos.x]


def bfs(grid, start_pos):
    visited = [start_pos]
    goals = []
    while visited != []:
        current_pos = visited.pop()
        current_val = get_pos(grid, current_pos)
        if current_val == 9:
            goals.append(current_pos)
        for d in DIRECTIONS:
            next_pos = current_pos + d
            # next node can be reached if it's value is current + 1
            if in_bounds(grid, next_pos) and get_pos(grid, next_pos) == current_val + 1:
                if next_pos not in visited:
                    visited.append(next_pos)
    return goals


def main(grid):
    trailheads = []
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == 0:
                trailheads.append(Vec2d(x, y))

    total = 0
    total2 = 0
    for start_pos in trailheads:
        trails = bfs(grid, start_pos)
        total += len(set(trails))
        total2 += len(trails)
    print("Part 1: ", total)
    print("Part 2: ", total2)

if __name__ == "__main__":
    import sys
    infile = sys.argv[1] if 1 < len(sys.argv) else "example.txt"
    with open(infile) as f:
        grid = [list(map(int, list(l.rstrip()))) for l in f.readlines()]
        main(grid)

