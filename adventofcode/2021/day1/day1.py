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


def part1(infile):
    with open(infile) as f:
        lines = f.readlines()
        previous = int(lines[0])
        i = 0
        for line in lines[1:]:
            if int(line) > previous:
                i += 1
            previous = int(line)
        print("Part 1 ", i)



def part2(infile):
    with open(infile) as f:
        lines = f.readlines()
        previous = None
        i = 0
        for w in window(lines):
            measure = sum(int(x) for x in w)
            if previous is not None and  measure > previous:
                i += 1
            previous = measure
        print("Part 2 ", i)


if __name__ == "__main__":
    import sys
    infile = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
    part1(infile)
    part2(infile)
