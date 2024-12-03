#!/usr/bin/env python3
from collections import defaultdict
from array import array


def main(initial_suite, max_iteration):
    iteration = 1
    seen = defaultdict(int)

    # init
    for number in initial_suite:
        seen[number] = iteration
        iteration += 1

    current = 0
    while iteration < max_iteration:
        last_seen = seen[current]
        if last_seen == 0:
            seen[current] = iteration
            current = 0  # next
        else:
            seen[current] = iteration
            current = iteration - last_seen  # next
        iteration += 1
    return current


def main_array(initial_suite, max_iteration):
    iteration = 1
    seen = array('I', [0] * max_iteration)

    # init
    for number in initial_suite:
        seen[number] = iteration
        iteration += 1

    current = 0
    while iteration < max_iteration:
        last_seen = seen[current]
        if last_seen == 0:
            seen[current] = iteration
            current = 0  # next
        else:
            seen[current] = iteration
            current = iteration - last_seen  # next
        iteration += 1
    return current




if __name__ == "__main__":
    inp = [6, 3, 15, 13, 1, 0]
    # 423 µs ± 53.9 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
    print(main(inp, 2020))
    # 13.6 s ± 2.89 s per loop (mean ± std. dev. of 7 runs, 1 loop each)
    #print(main(inp, 30000000))
    print(main_array(inp, 30000000))
