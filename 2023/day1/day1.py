def part1(lines): 
    res = []

    for line in lines:
        digits = [c for c in line if c.isnumeric()]
        res.append(int(digits[0] + digits[-1]))

    print(f"Part 1: {sum(res)}")


spelled_digits = { "one": "o1e", "two": "t2o", "three": "t3e", "four": "f4r", "five": "f5e", "six": "s6x", "seven": "s7n", "eight": "e8t", "nine": "n9e" }


def substitute_digits(s, trans):
    res = s
    for word, digit in trans.items():
        res = res.replace(word, digit)
    return res


def part2(lines): 
    res = []

    for line in lines:
        line = line.rstrip()
        res_line = []

        nline = ""
        for c in line:
            nline += c
            nline = substitute_digits(nline, spelled_digits)

        digits = [c for c in nline if c.isnumeric()]
        r = int(digits[0] + digits[-1])
        print(f"{line} => {nline}, {r}")
        res.append(r)

    print(f"Part 2: {sum(res)}")


if __name__ == "__main__":
    import sys
    infile = sys.argv[1]
    
    with open(infile) as f:
        lines = f.readlines()
        part1(lines)
        part2(lines)
