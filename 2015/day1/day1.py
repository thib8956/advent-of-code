#!/usr/bin/env python3
def main(inp):
    floor = 0
    basement = -1
    for i, c in enumerate(inp):
        if c == "(": floor += 1
        elif c == ")": floor -= 1
        if basement == -1 and floor == -1:
            basement = i + 1
    print("Part 1: ", floor)
    print("Part 2: ", basement)

    
if __name__ == '__main__':
    import sys
    infile = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
    with open(infile) as inp:
        main(inp.read().rstrip())

