from collections import Counter


def part2(ids):
    for id_a in ids:
        for id_b in ids:
            common_letters = [a for a, b in zip(id_a, id_b) if a == b]
            if len(common_letters) == len(id_a) - 1:
                res = "".join(common_letters)
                print("Part 2: ", res)
                return


def main(lines):
    total_twice, total_thrice = 0, 0
    for line in lines:
        c = Counter(line)
        total_twice += 1 if [k for k,v in c.items() if v == 2] != [] else 0
        total_thrice += 1 if [k for k,v in c.items() if v == 3] != [] else 0
    print(f"Part 1: ", total_twice * total_thrice)

    part2(lines)


if __name__ == "__main__":
    import sys
    infile = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
    with open(infile) as inp:
        main([l.rstrip() for l in inp.readlines()])

