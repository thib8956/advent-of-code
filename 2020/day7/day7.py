#!/usr/bin/env python3
import re
from collections import defaultdict, deque


def main(inp):
    with open(inp) as input_rules:
        rules = parse_rules(input_rules)
        reverse_rules = build_reverse_rules(rules)
        print(part1(reverse_rules))
        print(part2(rules, "shiny gold"))


def parse_rules(input_rules):
    rules = {}
    for input_rule in input_rules:
        color, rule = input_rule.split(" bags contain ")
        rules[color] = {color: int(number) for number, color in re.findall('(\d+) (\w+ \w+)', rule)}
    return rules


def build_reverse_rules(rules):
    reverse_rules = defaultdict(list)
    for bag, inner_rules in rules.items():
        for c in inner_rules:
            reverse_rules[c].append(bag)
    return reverse_rules


def part1(reverse_rules):
    queue  = deque(("shiny gold",))
    may_contain_shiny_gold = set()
    while queue:
        color = queue.pop()
        for c in reverse_rules.get(color, []):
            if c not in may_contain_shiny_gold:
                may_contain_shiny_gold.add(c)
                queue.appendleft(c)
    return len(may_contain_shiny_gold)


def part2(rules, color):
    return sum(number + number * part2(rules, c) for c, number in rules[color].items())


if __name__ == "__main__":
    main("input.txt")
