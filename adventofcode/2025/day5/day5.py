#!/usr/bin/env python3
import fileinput


def ingredient_is_fresh(ingredient, id_ranges):
    for range in id_ranges:
        start, end = range
        if start <= ingredient <= end:
            return True
    return False


def merge_ranges(ranges):
    "Merge overlapping ranges"
    # sort ranges by start value
    ranges.sort(key=lambda x: x[0])
    queue = [ranges[0]]
    for range in ranges[1:]:
        current_start, end = range
        last_start, last_end = queue.pop()
        if current_start <= last_end:  # overlap
            start = last_start
            end = max(last_end, end)
            queue.append((start, end))
        else:  # no overlap
            queue.append((last_start, last_end))
            queue.append((current_start, end))
    return queue


def main(inp):
    sep = inp.index("")
    id_ranges = [tuple(map(int, x.split("-"))) for x in inp[:sep]]
    id_ranges = merge_ranges(id_ranges)
    available_ids = (int(x) for x in inp[sep + 1 :])

    # Part 1
    total = 0
    for ingredient in available_ids:
        if ingredient_is_fresh(ingredient, id_ranges):
            total += 1
    print("Part 1:", total)

    # Part 2
    total = 0
    for range in id_ranges:
        start, end = range
        total += end - start + 1
    print("Part 2: ", total)


if __name__ == "__main__":
    lines = [x.rstrip() for x in fileinput.input()]
    main(lines)
