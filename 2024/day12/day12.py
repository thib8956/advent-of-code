from dataclasses import dataclass
from collections import defaultdict


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


def visit_region(grid, root):
    region = set()
    # BFS
    queue = [root]
    visited = set()
    region.add(root)
    visited.add(root)

    while queue != []:
        node = queue.pop(0)
        for d in DIRECTIONS:
            new_pos = node + d
            if in_bounds(grid, new_pos) and new_pos not in visited:
                visited.add(new_pos)
                if grid[root.y][root.x] == grid[new_pos.y][new_pos.x]:
                    queue.append(new_pos)
                    region.add(new_pos)

    return region
 

def get_perimeter(grid, region):
    perimeter = 0
    for node in region:
        for d in DIRECTIONS:
            new_pos = node + d
            if not in_bounds(grid, new_pos) or grid[new_pos.y][new_pos.x] != grid[node.y][node.x]:
                perimeter += 1
    return perimeter


def main(grid):
    # build list of regions using BFS
    regions = []
    visited = set()
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            pos = Vec2d(x, y)
            if pos not in visited:
                region = visit_region(grid, pos)
                visited.update(region)
                regions.append((c, region))

    total = 0
    for region in regions:
        c, nodes = region
        area = len(nodes)
        perimeter = get_perimeter(grid, nodes)
        #print(f"Region {c} area {area} perimeter {perimeter}")
        total += area * perimeter
    print("Part 1: ", total)

if __name__ == "__main__":
    import sys
    infile = sys.argv[1] if 1 < len(sys.argv) else "example.txt"
    with open(infile) as f:
        grid = [l.rstrip() for l in f.readlines()]
        main(grid)

