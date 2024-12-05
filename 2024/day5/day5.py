from collections import defaultdict
from itertools import pairwise


def check_update(upd, rules):
    for a, b in pairwise(upd):
        if [a, b] not in rules:
            return False
    return True
        


def main(content):
    order, updates = content.split("\n\n")
    order = [x.split("|") for x in order.split("\n")]
    updates = [x.split(",") for x in updates.rstrip().split("\n")]

    part1 = 0
    for update in updates:
        if check_update(update, order):
            middle = update[len(update)//2]
            part1 += int(middle)
    print("Part 1: ", part1)


if __name__ == "__main__":
    import sys
    infile = sys.argv[1] if 1 < len(sys.argv) else "example.txt"
    with open(infile) as f:
        main(f.read())

