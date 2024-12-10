def test(values, part2=False):
    if len(values) == 1:
        yield values[0]
    else:
        for rest in test(values[1:], part2):
            yield values[0] + rest
            yield values[0] * rest
            if part2:
                yield int(str(rest) + str(values[0]))  # concatenation


def main(data):
    part1 = 0
    part2 = 0
    for expected, values in data:
        for res in test(values[::-1]):
            if res == expected:
                part1 += res
                break
        for res in test(values[::-1], part2=True):
            if res == expected:
                part2 += res
                break

    print("Part 1: ", part1)
    print("Part 2: ", part2)


if __name__ == "__main__":
    import sys
    infile = sys.argv[1] if 1 < len(sys.argv) else "example.txt"
    with open(infile) as f:
        data = [l.rstrip().split(": ") for l in f.readlines()]
        data = [(int(a), tuple(map(int, b.split(" ")))) for a, b in data]
        main(data)

