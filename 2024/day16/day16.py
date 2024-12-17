from dataclasses import dataclass
from heapq import heappop, heappush


DIRECTIONS = {
    ">": 1 + 0j,  # EAST
    "v": 0 + 1j,  # SOUTH
    "<": -1 + 0j,  # WEST
    "^": 0 - 1j,  # NORTH
}

DIRECTIONS_RV = {v: k for k,v in DIRECTIONS.items()}


@dataclass(frozen=True)
class Node:
    pos: complex
    direction: complex
    cost: int = 0
    parent: "Node" = None

    def __lt__(self, other):
        return self.cost < other.cost


def find_start_and_goal(grid):
    start, goal = None, None
    for y, row in enumerate(grid):
        for x, _ in enumerate(row):
            if grid[y][x] == "S":
                start = complex(x, y)
            elif grid[y][x] == "E":
                goal = complex(x, y)
    return start, goal


def get_pos(grid, pos):
    x, y = int(pos.real), int(pos.imag)
    if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
        return grid[y][x]
    return None


def search(grid, start_node, end_pos):
    """
    Returns the shortest path between start and end using Dijkstra's algorithm
    """
    queue = [start_node]
    visited = set()
    best_costs = {}
    while queue != []:
        node = heappop(queue)
        visited.add(node)

        if node.pos == end_pos:
            return node

        if node.cost > best_costs.get((node.pos, node.direction), 99999999):  # already found a better path to this pos
            continue

        best_costs[(node.pos, node.direction)] = node.cost

        # visit each neighbor
        # go in the same direction
        n1 = Node(node.pos + node.direction, node.direction, node.cost + 1, node)
        if get_pos(grid, n1.pos) != "#" and n1 not in visited:
            heappush(queue, n1)
        # turn clockwise
        turned = node.direction * 1j
        n2 = Node(node.pos + turned, turned, node.cost + 1000 + 1, node)
        if get_pos(grid, n2.pos) != "#" and n2 not in visited:
            heappush(queue, n2)
        # turn counterclockwise
        turned = node.direction * -1j
        n3 = Node(node.pos + turned, turned, node.cost + 1000 + 1, node)
        if get_pos(grid, n3.pos) != "#" and n3 not in visited:
            heappush(queue, n3)

    return None


def print_grid(grid):
    for row in grid:
        print("".join(row))


def main(grid, debug=False):
    start, goal = find_start_and_goal(grid)
    direction = 1 + 0j  # initial direction is east
    end_node = search(grid, Node(start, direction), goal)
    total_cost = end_node.cost
    print("Part 1: ", total_cost)
    if debug:
        # compute path
        n = end_node
        path = []
        if n is not None:
            while n.parent is not None:
                path.insert(0, n)
                n = n.parent

        for n in path:
            x, y = int(n.pos.real), int(n.pos.imag)
            grid[y][x] = "O"
            print(f"Pos {x},{y} Direction {DIRECTIONS_RV[n.direction]} Cost {n.cost}")
            print_grid(grid)
            input()
            print(chr(27) + "[2J")  # clear terminal
        

if __name__ == "__main__":
    import sys
    infile = sys.argv[1] if 1 < len(sys.argv) else "example.txt"
    with open(infile) as f:
        grid = [list(l.rstrip()) for l in f.readlines()]
        main(grid)

