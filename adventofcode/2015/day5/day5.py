#!/usr/bin/env python3
from itertools import islice

VOWELS = "aeiou"
BAD = ["ab", "cd", "pq", "xy"]


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


def part1(inp):
    total = 0
    for line in inp:
        """
        - It contains at least three vowels (aeiou only), like aei, xazegov, or
        aeiouaeiouaeiou.
        - It contains at least one letter that appears twice in a row, like xx,
        abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
        - It does not contain the strings ab, cd, pq, or xy, even if they are
        part of one of the other requirements.
        """
        if any(x in line for x in BAD) or sum(1 for x in line if x in VOWELS) < 3:
            continue
        total += any(a == b for a, b in zip(line, line[1:]))
    print("Part 1: ", total)


def part2(inp):
    """
    - It contains a pair of any two letters that appears at least twice in the
    string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like
    aaa (aa, but it overlaps).
    - It contains at least one letter which repeats with exactly one letter
    between them, like xyx, abcdefeghi (efe), or even aaa.
    """
    total = 0
    for line in inp:
        has_repeat = False
        for triplet in window(line, n=3):
            if triplet[0] == triplet[2]:
                has_repeat = True
                break

        seen_pairs = set()
        has_pair = False
        prev_pair = None
        for pair in window(line, n=2):
            if pair in seen_pairs:
                has_pair = True
            else:
                # Add the previous pair to avoid overlapping
                if prev_pair is not None:
                    seen_pairs.add(prev_pair)
            prev_pair = pair
            if has_pair and has_repeat:
                break  # Early exit when both conditions are met

        if has_pair and has_repeat:
            total += 1

    print("Part 2: ", total)


if __name__ == "__main__":
    import fileinput

    lines = [x.rstrip() for x in fileinput.input()]
    part1(lines)
    part2(lines)
