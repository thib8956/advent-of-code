#!/usr/bin/env python3
import fileinput
from itertools import combinations


class UnionFind:
    """
    Two sets are called disjoint sets if they don't have any element in common.
    The disjoint set data structure is used to store such sets. It supports
    following operations:
    - Merging two disjoint sets to a single set using Union operation.
    - Finding representative of a disjoint set using Find operation.
    """

    def __init__(self, elements):
        # init each element to be its own parent
        self.parents = {e: e for e in elements}
        # keep track of the size of each component
        self.size = {e: 1 for e in elements}

    def find(self, a):
        if self.parents[a] != a:
            self.parents[a] = self.find(self.parents[a])  # compress path
        return self.parents[a]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        # attach smaller under larger (union by size)
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parents[rb] = ra
        self.size[ra] += self.size[rb]


def distance(first, second):
    xa, ya, za = first
    xb, yb, zb = second
    return (xa - xb) ** 2 + (ya - yb) ** 2 + (za - zb) ** 2


def part1(boxes, edges, N=1000):
    uf = UnionFind(boxes)
    # make the first N connections
    for _, a, b in edges[:N]:
        uf.union(a, b)
    sizes = sorted(uf.size.values(), reverse=True)
    total = sizes[0] * sizes[1] * sizes[2]
    return total


def part2(boxes, edges):
    uf = UnionFind(boxes)
    for _, a, b in edges:
        uf.union(a, b)
        # if we've connected all the boxes, we're done
        if max(uf.size.values()) == len(boxes):
            xa, _, _ = a
            xb, _, _ = b
            return xa * xb


def main(inp):
    boxes = [tuple(map(int, line.split(","))) for line in inp]
    edges = sorted((distance(a, b), a, b) for a, b in combinations(boxes, 2))
    if len(boxes) == 20:  # example input
        print("Part 1:", part1(boxes, edges, N=10))
        print("Part 2:", part2(boxes, edges))
    else:
        print("Part 1:", part1(boxes, edges))
        print("Part 2:", part2(boxes, edges))


if __name__ == "__main__":
    with fileinput.input() as f:
        main(f)
