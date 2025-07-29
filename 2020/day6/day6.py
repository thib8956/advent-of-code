#! /usr/bin/env python3
from collections import Counter


def part1(groups):
    number_of_questions = 0
    for group in groups:
        unique_questions = set(group.replace("\n", ""))
        number_of_questions += len(unique_questions)
    print(number_of_questions)


def part2(groups):
    # number of questions for which everyone in a group answered 'yes'
    number_of_questions = 0
    for group in groups:
        group_length = group.count("\n") + 1
        group_counter = Counter(group.replace("\n", ""))
        everyone_answered = [k for (k, v) in group_counter.items() if v == group_length]
        number_of_questions += len(everyone_answered)
    print(number_of_questions)


if __name__ == "__main__":
    import sys
    inp = sys.argv[1]
    groups = open(inp).read().split("\n\n")
    part1(groups)
    part2(groups)

