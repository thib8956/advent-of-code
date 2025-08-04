from collections import Counter


def main(lines):
    firsts, seconds = list(sorted(x[0] for x in lines)), list(sorted(x[1] for x in lines))
    total = sum(abs(a - b) for (a, b) in zip(firsts, seconds))
    print("Part 1: ", total)

    counts = Counter(seconds)
    total = sum(x * counts[x] for x in firsts)
    print("Part 2: ", total)


if __name__ == "__main__":

    import sys
    infile = sys.argv[1]
    
    with open(infile) as f:
        lines = f.readlines()
        lines = [list(map(int, x.rstrip().split())) for x in lines]
        main(lines)

