#!/usr/bin/env python3
import re
import itertools
from dataclasses import dataclass
from collections import defaultdict


@dataclass
class Rectangle:
    x: int
    y: int
    width: int
    height: int

    @property
    def x2(self):
        return self.x + self.width

    @property
    def y2(self):
        return self.y + self.height


def parse_line(l):
    parsed = re.findall(r"\d+", l)
    id_, x, y, width, height = map(int, parsed)
    return id_, Rectangle(x, y, width, height)


def main(inp):
    regions = defaultdict(set)
    for id_, region in map(parse_line, inp):
        for x in range(region.x, region.x2):
            for y in range(region.y, region.y2):
                regions[x, y].add(id_)

    total = sum(len(x) > 1 for x in regions.values())
    print(f"Part 1: ", total)

    all_ids = set()
    overlapping_ids = set()
    for region in regions.values():
        all_ids.update(region)
        if len(region) > 1:
            overlapping_ids.update(region)
    difference = all_ids - overlapping_ids
    print(f"Part 2: {difference.pop()}")

    
if __name__ == '__main__':
    import sys
    infile = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
    with open(infile) as inp:
        main([l.rstrip() for l in inp.readlines()])

