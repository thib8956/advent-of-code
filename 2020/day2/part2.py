#! /usr/bin/env python3


def xor(a, b):
    return (a and not b) or (not a and b)


def parse_line(line):
    repeat_range, letter, pwd = line.split(' ')
    letter = letter[0]
    first_pos, second_pos = repeat_range.split('-')
    first_pos, second_pos = int(first_pos), int(second_pos)
    return letter, first_pos, second_pos, pwd


def test_password(line):
    letter, first_pos, second_pos, pwd = parse_line(line)
    return xor(pwd[first_pos - 1] == letter,
        pwd[second_pos - 1] == letter)


def main(passwds):
    valid_counter = 0
    for l in passwds:
        if test_password(l):
            valid_counter += 1
    print(f"Number of  valid password in input : {valid_counter}")

