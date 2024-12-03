def parse_input(infile):
    with open(infile) as f:
        return [[int(x) for x in l.strip().split()] for l in f.readlines()]


def process_line(line):
        if set(line) == {0}:
            return 0
        else:
            next_line = [cur - next for next, cur in zip(line, line[1:])]
            return line[-1] + process_line(next_line)


def process_line_back(line):
    if set(line) == {0}:
        return 0
    else:
        next_line = [cur - next for next, cur in zip(line, line[1:])]
        return line[0] - process_line_back(next_line)


def solve(data):
    print(f"Part 1: {sum(process_line(l) for l in data)}")
    print(f"Part 2: {sum(process_line_back(l) for l in data)}")


if __name__ == "__main__":
    import sys
    import os
    SCRIPTPATH = os.path.dirname(os.path.realpath(__file__))
    infile = sys.argv[1] if len(sys.argv) == 2 else "example.txt"
    data = parse_input(os.path.join(SCRIPTPATH, infile))
    solve(data)
