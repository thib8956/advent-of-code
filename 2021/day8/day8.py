def part1(inp):
    total = 0
    for display in inp:
        _, output_values = display
        for value in output_values:
            if len(value) in [2, 4, 3, 7]:
                total += 1
    print(f"Part 1 : {total}")


def part2(inp):
    for display in inp:
        patterns, values = display
        patterns = sorted(patterns, key=lambda x: len(x))
        print(patterns)
        # easy
        d1 = [x for x in patterns if len(x) == 2][0]
        print("1", d1)
        d4 = [x for x in patterns if len(x) == 4][0]
        print("4", d4)
        d7 = [x for x in patterns if len(x) == 3][0]
        print("7", d7)
        d8 = [x for x in patterns if len(x) == 7][0]
        print("8", d8)

        # 3 is the only digit that has all common segments with 1
        breakpoint()
        d3 = [x for x in patterns if set(d1).issubset(set(x)) and len(x) == 5][0]
        print("3", d3)

        break

def main(infile):
    inp = []
    with open(infile) as f:
        for display in f:
            display = display.rstrip().split(" | ")
            signal_patterns = display[0].split(" ")
            output_values = display[1].split(" ")
            inp.append([signal_patterns, output_values])
    part1(inp)
    part2(inp)


if __name__ == "__main__":
    import sys
    infile = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
    main(infile)
