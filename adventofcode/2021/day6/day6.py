from collections import defaultdict, Counter

def calculate_fishes(inp, days):
    fishes = Counter(inp)
    for day in range(days):
        fishes_new = defaultdict(int)
        for fish, cnt in fishes.items():
            if fish == 0:
                fishes_new[8] += cnt
                fishes_new[6] += cnt
            else:
                fishes_new[fish - 1] += cnt
        fishes = fishes_new
    return sum(fishes.values())
    

def main(infile):
    with open(infile) as f:
        inp = [int(x) for x in f.readline().split(",")]
    res = calculate_fishes(inp, 80)
    print(f"Part 1, {res}")
    res = calculate_fishes(inp, 256)
    print(f"Part 2, {res}")

if __name__ == "__main__":
    import sys
    infile = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
    main(infile)
