#!/usr/bin/env python3
import fileinput
from collections import defaultdict
from itertools import permutations


def parse_locations(inp: list[str]) -> dict[str, dict[str, int]]:
    "parse list of location pairs into adjacency map"
    locations = defaultdict(dict)
    for line in inp:
        places, dist = line.split(" = ")
        place_from, place_to = places.split(" to ")
        locations[place_from][place_to] = int(dist)
        locations[place_to][place_from] = int(dist)  # store both directions
    return locations


def main(inp):
    "brute force over permutations of cities, keeping track of min and max cost"
    locations = parse_locations(inp)
    min_cost = 99999
    max_cost = 0
    for perm in permutations(locations):
        cost = 0
        # iterate over pairs of cities and get cost from adjacency map
        for city_a, city_b in zip(perm, perm[1:]):
            cost += locations[city_a][city_b]
        min_cost = min(cost, min_cost)
        max_cost = max(cost, max_cost)
    print("Part 1: ", min_cost)
    print("Part 2: ", max_cost)


if __name__ == "__main__":
    lines = [x.rstrip() for x in fileinput.input()]
    main(lines)
