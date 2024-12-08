from collections import defaultdict
from itertools import pairwise


def check_update(upd, rules):
    for a, b in pairwise(upd):
        if [a, b] not in rules:
            return False
    return True

def fix_update(upd, rules):
    while not check_update(upd, rules):
        for i in range(len(upd)):
            for j in range(i+1, len(upd)):
                if [upd[j], upd[i]] in rules:
                    upd[j], upd[i] = upd[i], upd[j]

def main(content):
    rules, updates = content.split("\n\n")
    rules = [x.split("|") for x in rules.split("\n")]
    updates = [x.split(",") for x in updates.rstrip().split("\n")]

    part1 = 0
    incorrect_updates = []
    for update in updates:
        if check_update(update, rules):
            middle = update[len(update)//2]
            part1 += int(middle)
        else:
            incorrect_updates.append(update)
    print("Part 1: ", part1)

    part2 = 0
    for update in incorrect_updates:
        fix_update(update, rules)
        middle = update[len(update)//2]
        part2 += int(middle)
    print("Part 2: ", part2)


if __name__ == "__main__":
    import sys
    infile = sys.argv[1] if 1 < len(sys.argv) else "example.txt"
    with open(infile) as f:
        main(f.read())
