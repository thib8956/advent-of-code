from typing import Dict, List, Set, Tuple
from dataclasses import dataclass
from collections import defaultdict
from enum import Enum


@dataclass(frozen=True)
class Vec2d:
    x: int
    y: int

    def __add__(self, other): 
        return Vec2d(self.x + other.x, self.y + other.y)


class Direction(Enum):
    NORTH = Vec2d(0, -1)  # [0, 0] is the top-left corner, so y increases going downwards
    SOUTH = Vec2d(0, 1)
    EAST = Vec2d(1, 0)
    WEST = Vec2d(-1, 0)


"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
"""
PIPES = {
    "|": (Direction.SOUTH, Direction.NORTH),
    "-": (Direction.EAST, Direction.WEST),
    "L": (Direction.NORTH, Direction.EAST),
    "J": (Direction.NORTH, Direction.WEST),
    "7": (Direction.SOUTH, Direction.WEST),
    "F": (Direction.SOUTH,Direction.EAST),
}

PIPES_REVERSE_LOOKUP = {v: k for k,v in PIPES.items()}


def find_start_position(grid: List[str]) -> Vec2d:
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == "S":
                return Vec2d(x, y)
    raise RuntimeError("The start position was not found")


def update_start_symbol(grid: List[str], start_pos: Vec2d):
    """
    Updates the map by replacing the start symbol "S" with its actual corresponding pipe
    """
    # check which neighbors are connected to the start position
    connections = [] 
    north = start_pos + Direction.NORTH.value
    south = start_pos + Direction.SOUTH.value
    east = start_pos + Direction.EAST.value
    west = start_pos + Direction.WEST.value

    if grid[north.y][north.x] in "|7F":
        connections.append(Direction.NORTH)

    if grid[south.y][south.x] in "|LJ":
        connections.append(Direction.SOUTH)

    if grid[east.y][east.x] in "-7J":
        connections.append(Direction.EAST)

    if grid[west.y][west.x] in "-LF":
        connections.append(Direction.WEST)

    print("Start symbol has the following connections: ", connections)
    assert len(connections) == 2, "start symbol has invalid connections"
    pipe = PIPES_REVERSE_LOOKUP[tuple(connections)]
    print(f"Start symbol is a {pipe} pipe")

    # replace it in the grid accordingly
    grid[start_pos.y] = grid[start_pos.y].replace("S", pipe)


def parse_graph(grid: List[str]) -> Dict[Vec2d, List[Vec2d]]:
    graph = defaultdict(list)

    for y, row in enumerate(grid):
        for x, pipe in enumerate(row):
            pos = Vec2d(x, y)
            if pipe in PIPES:
                for direction in PIPES[pipe]:
                    next_pos = pos + direction.value
                    graph[pos].append(next_pos)
    return graph


def traverse_graph(graph, start_pos) -> Tuple[int, Set[Vec2d]]:
    """
    traverse the graph using BFS, return the path and the
    find the length of the longest path in the graph
    """
    queue = [(start_pos, 0)]  # (pos, distance from start)
    max_dist = 0
    visited = {start_pos}

    while queue != []:
        cur, dist = queue.pop(0)
        max_dist = max(max_dist, dist)

        for next_pos in graph[cur]:
            if next_pos not in visited:
                visited.add(next_pos)
                queue.append((next_pos, dist+1))

    return max_dist, visited


def count_enclosed_tiles(grid, edges):
    """
    count the number of enclosed tiles in the loop by casting a ray on each row
    and counting the number of intersections with the edges of the loop
    """
    enclosed_count = 0
    for y, row in enumerate(grid):
        crossings = 0
        for x, pipe in enumerate(row):
            pos = Vec2d(x, y)
            if pos in edges:
                if pipe in "L|J":
                    crossings += 1
            elif crossings % 2 == 1:
                enclosed_count += 1
    return enclosed_count


def main(grid):
    rows, cols = len(grid), len(grid[0])
    start_pos = find_start_position(grid)
    print("Start pos ", start_pos)
    update_start_symbol(grid, start_pos)
    graph = parse_graph(grid)

    max_dist, visited = traverse_graph(graph, start_pos)
    print("Part 1: ", max_dist)

    # visited edges are the ones that are part of the loop
    inside_count = count_enclosed_tiles(grid, visited)
    print("Part 2: ", inside_count)


if __name__ == "__main__":
    import sys
    infile = sys.argv[1]
    
    with open(infile) as f:
        lines = [l.rstrip() for l in f.readlines()]
        main(lines)
