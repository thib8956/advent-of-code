#!/usr/bin/env python3
import fileinput
import re
from functools import reduce
from itertools import combinations
from operator import mul


def parse_ingredients(inp):
    ingredients = []
    for line in inp:
        ingredients.append(tuple(map(int, re.findall(r"(-?\d+)", line))))
    return ingredients


def generate_combinations():
    "Generate combinations of length 4 that sum to 100"
    for x, y, z in combinations(range(1, 100), 3):
        a = x
        b = y - x
        c = z - y
        d = 100 - z
        yield (a, b, c, d)


def example(ingredients):
    # for example input, two ingredients such that
    # a + b = 100 with a and b >= 0
    max_score = 0
    for a in range(0, 101):
        b = 100 - a
        # ignore last property (calories)
        qty_a = [x * a for x in ingredients[0][:-1]]
        qty_b = [x * b for x in ingredients[1][:-1]]
        props = [x + y if x + y > 0 else 0 for x, y in zip(qty_a, qty_b)]
        score = reduce(mul, props)
        max_score = max(score, max_score)
    return max_score


def example_part2(ingredients):
    max_score = 0
    for a in range(0, 101):
        b = 100 - a
        qty_a = [x * a for x in ingredients[0]]
        qty_b = [x * b for x in ingredients[1]]
        # check calories == 500
        if qty_a[-1] + qty_b[-1] != 500:
            continue
        props = [x + y if x + y > 0 else 0 for x, y in zip(qty_a, qty_b)]
        score = reduce(mul, props[:-1])
        max_score = max(score, max_score)
    return max_score


def part1(ingredients):
    max_score = 0
    for a, b, c, d in generate_combinations():
        qty_a = [x * a for x in ingredients[0][:-1]]
        qty_b = [x * b for x in ingredients[1][:-1]]
        qty_c = [x * c for x in ingredients[2][:-1]]
        qty_d = [x * d for x in ingredients[3][:-1]]
        props = [
            x + y + z + w if x + y + z + w > 0 else 0
            for x, y, z, w in zip(qty_a, qty_b, qty_c, qty_d)
        ]
        score = reduce(mul, props)
        max_score = max(score, max_score)
    return max_score


def part2(ingredients):
    max_score = 0
    for a, b, c, d in generate_combinations():
        qty_a = [x * a for x in ingredients[0]]
        qty_b = [x * b for x in ingredients[1]]
        qty_c = [x * c for x in ingredients[2]]
        qty_d = [x * d for x in ingredients[3]]
        props = [
            x + y + z + w if x + y + z + w > 0 else 0
            for x, y, z, w in zip(qty_a, qty_b, qty_c, qty_d)
        ]
        # check calories == 500
        calories = sum(x[-1] for x in [qty_a, qty_b, qty_c, qty_d])
        if calories != 500:
            continue
        score = reduce(mul, props[:-1])
        max_score = max(score, max_score)
    return max_score


def main(inp):
    ingredients = parse_ingredients(inp)
    if len(ingredients) == 2:  # example
        print("Part 1: ", example(ingredients))
        print("Part 2: ", example_part2(ingredients))
    else:
        print("Part 1: ", part1(ingredients))
        print("Part 2: ", part2(ingredients))


if __name__ == "__main__":
    with fileinput.input() as f:
        lines = [x.rstrip() for x in fileinput.input()]
    main(lines)
