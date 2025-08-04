#! /usr/bin/env python3
import re


def main(inp):
    inp = open(inp).read().rstrip().split('\n\n')
    valid_passeports_1, valid_passeports_2 = 0, 0
    for l in inp:
        l = re.split(r'[\n\s]', l)
        passeport = dict(p.split(':') for p in l)
        if check_passeport(passeport):
            valid_passeports_1 += 1
        if check_passeport(passeport, run_validators=True):
            valid_passeports_2 += 1
    print("Part 1: valid passeports: ", valid_passeports_1)
    print("Part 2: valid passeports: ", valid_passeports_2)


def check_passeport(passeport, run_validators=False):
    fields = [
        ('byr', lambda v: 1920 <= int(v) <= 2002), # (Birth Year)
        ('iyr', lambda v: 2010 <= int(v) <= 2020),  # (Issue Year)
        ('eyr', lambda v: 2020 <= int(v) <= 2030),  # (Expiration Year)
        ('hgt', validate_height),  # (Height)
        ('hcl', lambda v: re.search("#[0-9a-f]{6}", v)),  # (Hair Color)
        ('ecl', lambda v: v in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')),  # (Eye Color)
        ('pid', lambda v: len(v) == 9 and v.isdecimal()),  # (Passport ID)
        #'cid'  # Country id, ignored
    ]
    for field, validator in fields:
            value = passeport.get(field)
            if value is None:
                return False
            elif run_validators and not validator(value):
                return False
    return True


def validate_height(v):
    unit = v[-2:]
    height = int(v[:-2])
    if unit == 'cm':
        return 150 <= height <= 193
    if unit == 'in':
        return 59 <= height <= 76
    return False


if __name__ == "__main__":
    import sys
    main(sys.argv[1])

