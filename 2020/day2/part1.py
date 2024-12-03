#! /usr/bin/env python3


def parse_line(line):
    repeat_range, letter, pwd = line.split(' ')
    letter = letter[0]
    repeat_min, repeat_max = repeat_range.split('-')
    repeat_min, repeat_max = int(repeat_min), int(repeat_max)
    return letter, range(repeat_min, repeat_max + 1), pwd


def test_password(line):
    letter, repeat_range, pwd = parse_line(line)
    count = pwd.count(letter)
    return count in repeat_range


def main(inp):
    with open(inp) as passwds:
        valid_counter = 0
        for l in passwds:
            if test_password(l):
                valid_counter += 1
        print(f"Number of  valid password in input : {valid_counter}")
        

if __name__ == "__main__":
    main('./input.txt')
