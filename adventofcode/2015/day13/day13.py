#!/usr/bin/env python3
import fileinput
from collections import defaultdict
from itertools import permutations


def parse_table_seating(inp):
    inp = [x.split() for x in inp]
    adj = defaultdict(dict)
    for line in inp:
        person_a, gain, amount, person_b = line[0], line[2], line[3], line[-1]
        adj[person_a][person_b.rstrip(".")] = (
            int(amount) if gain == "gain" else -int(amount)
        )
    return adj


def get_max_happiness(seatings):
    max_happiness = 0
    for perm in permutations(seatings):
        # print(perm)
        # iterate over pairs of persons, while wrapping around (circular table)
        # calculate happiness for each pair
        happiness = 0
        for a, b in zip(perm, perm[1:] + perm[:1]):
            # print(a, b, seatings[a][b])
            # print(b, a, seatings[b][a])
            happiness += seatings[a][b] + seatings[b][a]
        max_happiness = max(happiness, max_happiness)
    return max_happiness


def main(inp):
    seatings = parse_table_seating(inp)
    max_happiness = get_max_happiness(seatings)
    print("Part 1: ", max_happiness)

    adj2 = seatings.copy()
    for p in seatings.keys():
        adj2[p]["Me"] = 0
        adj2["Me"][p] = 0
    max_happiness = get_max_happiness(adj2)
    print("Part 2: ", max_happiness)


if __name__ == "__main__":
    lines = [x.rstrip() for x in fileinput.input()]
    main(lines)
