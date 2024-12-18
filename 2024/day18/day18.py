from dataclasses import dataclass
from heapq import heappush, heappop


DIRECTIONS = (
    1 + 0j,  # EAST
    0 + 1j,  # SOUTH
    -1 + 0j,  # WEST
    0 - 1j,  # NORTH
)


@dataclass(frozen=True)
class Node:
    pos: complex
    cost: int = 0

    def __lt__(self, other):
        return self.cost < other.cost


def can_reach(pos, obstacles, grid_size):
    height, width = grid_size
    x, y = int(pos.real), int(pos.imag)
    if 0 <= x < width and 0 <= y < height:
        if (x, y) not in obstacles:
            return True
    return False


def search(obstacles, start, goal, grid_size):  # could just use bfs?
    queue = [Node(start)]
    visited = set()
    i = 0
    while queue != []: 
        node = heappop(queue)
        visited.add(node.pos)
        if node.pos == goal:
            return node.cost
        for direction in DIRECTIONS:
            new_pos = node.pos + direction
            n = Node(new_pos, node.cost + 1)
            if n not in queue and n.pos not in visited and can_reach(n.pos, obstacles, grid_size):
                heappush(queue, n)
    return -1


def find_path(coords, limit, grid_size):
    obstacles = coords[:limit]
    start = 0+0j
    goal = complex(grid_size[0] - 1, grid_size[1] - 1)
    cost = search(obstacles, start, goal, grid_size)
    return cost


def main(coords, limit, grid_size):
    part1 = find_path(coords, limit, grid_size)
    print("Part 1: ", part1)

    # binary search for part 2
    low, high = limit, len(coords)
    while high - low > 1:
        i = (low + high) // 2
        if find_path(coords, i, grid_size) != -1: 
            low = i
        else:
            high = i
    print("Part 2: ", coords[low])


if __name__ == "__main__":
    import sys
    infile = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
    with open(infile) as f:
        lines = f.readlines()
        lines = [tuple(map(int, l.rstrip().split(","))) for l in lines]
        if infile == "example.txt":
            main(lines, 12, (7, 7))
        else:
            main(lines, 1024, (71, 71))

