#!/usr/bin/env python3
import itertools


def main(inp):
    # Part 1
    changes = [int(n) for n in inp]
    print(sum(changes))
    freq = 0
    seen = {0}
    for num in itertools.cycle(changes):
        freq += num
        if freq in seen:
            print(freq)
            break
        seen.add(freq)

    
if __name__ == '__main__':
    import sys
    infile = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
    with open(infile) as inp:
        main(inp.readlines())

