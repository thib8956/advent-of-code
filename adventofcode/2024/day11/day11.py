from collections import Counter

def main(data):
    part1 = run(data, 25)
    print("Part 1: ", part1)
    part2 = run(data, 75)
    print("Part 2: ", part2)


def run(data, steps):
    data = Counter(data)
    for _ in range(steps):
        data = blink(data)
    return data.total()


def blink(data):
    new_counter = Counter()
    for stone, count in data.items():
        s = str(stone)
        if stone == 0:
            new_counter[1] += count
        elif len(s) % 2 == 0:
            first, second = int(s[:len(s)//2]), int(s[len(s)//2:])
            new_counter[first] += count
            new_counter[second] += count
        else:
            new_counter[2024*stone] += count
    return new_counter


if __name__ == "__main__":
    res = run((125, 17), 25) 
    assert res == 55312, f"expected 55312, but was {res}"

    import sys
    if len(sys.argv) > 1:
        infile = sys.argv[1]
        with open(infile) as f:
            data = tuple(map(int, f.read().rstrip().split()))
            main(data)
            
