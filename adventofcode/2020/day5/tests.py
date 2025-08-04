#! /usr/bin/env python3
from day5 import *

def tests():
    inputs = {
        "FBFBBFFRLR": (44, 5, 357),
        "BFFFBBFRRR": (70, 7, 567),
        "FFFBBBFRRR": (14, 7, 119),
        "BBFFBBFRLL": (102, 4, 820)
    }

    test("bisect", inputs)
    test("binary", inputs)


def test(strategy, inputs):
    for boarding_pass, expected in inputs.items():
        row, col = parse_boarding_pass(boarding_pass, strategy=strategy)
        seat_id =  get_seat_id(row, col)
        assert row == expected[0]
        assert col == expected[1]
        assert seat_id == expected[2]
        print(row, col, seat_id, expected)


if __name__ == "__main__":
    tests()
