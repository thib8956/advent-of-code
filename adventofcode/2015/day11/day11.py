#!/usr/bin/env python3
import fileinput
from itertools import islice


def window(seq, n=3):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result


def inc_string(s):
    """
    Increase the rightmost letter one step; if it was z, it wraps around to a,
    and repeat with the next letter to the left until one doesn't wrap around.
    """
    s = list(s)
    for i in range(len(s) - 1, -1, -1):
        if s[i] == "z":
            s[i] = "a"
        else:
            s[i] = chr(ord(s[i]) + 1)
            break
    return "".join(s)


def is_valid(pwd):
    """
    A valid password:
        - contains a increasing straight of three letters (abc, bcd, cde)
        - contains two distinct pairs of letters (aa, bb, or zz).
        - does not contain the letters i, o, or l.
    """
    has_forbiden_letters = any(x in "iol" for x in pwd)
    pairs = set(pwd[i + 1] for i in range(len(pwd) - 1) if pwd[i] == pwd[i + 1])
    has_two_pairs = len(pairs) == 2
    has_increasing_triplet = False
    for a, b, c in window(pwd):
        a, b, c = ord(a), ord(b), ord(c)
        if a + 1 == b and b + 1 == c:
            has_increasing_triplet = True
            break
    is_valid = not has_forbiden_letters and has_two_pairs and has_increasing_triplet
    return is_valid


def get_next_valid_pwd(pwd):
    while True:
        pwd = inc_string(pwd)
        if is_valid(pwd):
            return pwd


def main(pwd):
    pwd = get_next_valid_pwd(pwd)
    print("Part 1: ", pwd)
    pwd = get_next_valid_pwd(pwd)
    print("Part 2: ", pwd)


def test():
    assert inc_string("xx") == "xy"
    assert inc_string("xy") == "xz"
    assert inc_string("xz") == "ya"
    assert inc_string("ya") == "yb"


if __name__ == "__main__":
    line = next(x.rstrip() for x in fileinput.input())
    main(line)
