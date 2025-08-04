#!/usr/bin/env python3
import re
from collections import defaultdict, Counter
from pprint import pprint


def main(inp):
    # total minutes asleep per guard
    guards = defaultdict(int)
    # list of guards sleeping for each minute
    minutes = defaultdict(lambda: defaultdict(int))
    for l in sorted(inp):
        minute = re.search(r":(\d+)", l).group(1)
        if "#" in l:
            current_id = re.search(r"#(\d+)", l).group(1)
        elif "asleep" in l:
            start = int(minute)
        elif "wakes" in l:
            end = int(minute)
            guards[current_id] += end - start
            for m in range(start, end):
                minutes[m][current_id] += 1

    # Find the guard that has the most minutes asleep. What minute does that guard spend asleep the most?
    guard_id = max(guards.items(), key=lambda x: x[1])[0]
    minute = max([(k, v[guard_id]) for k, v in minutes.items() if guard_id in v], key=lambda x: x[1])[0]
    print("Part 1: ", int(guard_id) * minute)

    # Of all guards, which guard is most frequently asleep on the same minute?
    maxs = { m: max(minutes[m].items(), key=lambda x: x[1]) for m in minutes.keys()}
    minute, rest = max(maxs.items(), key=lambda x: x[1][1])
    id_, _ = rest
    print("Part 2: ", int(id_) * minute)


if __name__ == '__main__':
    import sys
    infile = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
    with open(infile) as inp:
        main(inp.readlines())

