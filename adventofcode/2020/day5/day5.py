#! /usr/bin/env python3
from itertools import product
from bisect import bisect


def main(inp):
    results = {}
    for line in inp:
        boarding_pass = line.rstrip()
        row, col = parse_boarding_pass(boarding_pass)
        seat_id = get_seat_id(row, col)
        results[boarding_pass] = (row, col, seat_id)
    part1(results)
    part2(results)


def part1(results):
    max_seat_id = max(x[2] for x in results.values())
    print("Max seat ID: ", max_seat_id)


def part2(results):
    seat_ids = sorted(x[2] for x in results.values())
    missing_seat_ids = set(range(max(seat_ids))) - set(seat_ids)
    print("Your seat id : ", max(missing_seat_ids))


def parse_boarding_pass(boarding_pass, strategy="binary"):
    "Poor man's dispatcher"
    try: 
        to_call = globals()[f"parse_boarding_pass_{strategy}"]
        return to_call(boarding_pass)
    except KeyError:
        raise KeyError(f"Bad strategy name {strategy}")


def parse_boarding_pass_binary(boarding_pass):
    "Parse boarding pass using a binary conversion"
    boarding_pass = boarding_pass.translate(str.maketrans("FLBR", "0011"))
    row = boarding_pass[:7]
    col = boarding_pass[7:]
    return int(row, base=2), int(col, base=2)


def parse_boarding_pass_bisect(boarding_pass):
    "Pass boarding pass using bisection algorithm"
    row = bisect(boarding_pass[:7], lower_option="F", upper_option="B", max=127)
    col = bisect(boarding_pass[7:], lower_option="L", upper_option="R", max=7)
    return row, col


def bisect(inp, lower_option, upper_option, max):
    min_v, max_v = 0, max
    for l in inp:
        length = max_v - min_v
        if l == lower_option:
            max_v = min_v + length // 2
        elif l == upper_option:
            min_v = 1 + min_v + length // 2
    return min_v

def get_seat_id(row, col):
    return 8 * row + col


if __name__ == "__main__":
    import fileinput
    main(fileinput.input())
