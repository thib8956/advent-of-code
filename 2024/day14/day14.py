from math import prod
from collections import Counter


def parse_bots(lines):
    lines = [l.rstrip().split(" ") for l in lines]
    lines = [complex(*map(int, x.split("=")[1].split(","))) for l in lines for x in l]
    return [lines[i:i+2] for i in range(0, len(lines), 2)] # [(pos, velocity), ...]


def simulate_bots(bots, grid_size, steps=100):
    step = 0
    width, height = grid_size
    while step < steps:
        new_bots = []
        for pos, velocity in bots:
            pos = pos + velocity
            if pos.real >= width:
                pos -= width
            if pos.real < 0:
                pos += width
            if pos.imag >= height:
                pos -= height * 1j
            if pos.imag < 0:
                pos += height * 1j
            new_bots.append((pos, velocity))
        bots = new_bots
        step += 1
    return [pos for pos, _ in bots]


def determine_quadrant(pos, grid_size):
    width, height = grid_size
    q = None
    if pos.real < width // 2 and pos.imag < height // 2:
        q = 0
    elif pos.real > width // 2 and pos.imag < height //2:
        q = 1
    elif pos.real < width // 2 and pos.imag > height // 2:
        q = 2
    elif pos.real > width // 2 and pos.imag > height // 2:
        q = 3
    return q


def part1(bots, grid_size):
    bots = simulate_bots(bots, grid_size)
    c = Counter(bots)
    total_quadrants = [0, 0, 0, 0]
    for pos, count in c.items():
        q = determine_quadrant(pos, grid_size)
        if q is None:  # ignore middle row and col
            continue
        total_quadrants[q] += count
    #print_grid(c, grid_size)
    return prod(total_quadrants)


def main(lines):
    bots = parse_bots(lines)
    total = part1(bots, grid_size)
    print("Part 1: ", total)


def print_grid(c, grid_size):
    width, height = grid_size
    for y in range(height):
        for x in range(width):
            a = c.get(complex(x, y))
            if a is None:
                print(".", end="")
            else:
                print(a, end="")
        print()

        
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        infile = "example.txt"
        grid_size = (11, 7)
    else:
        infile = sys.argv[1]
        grid_size = (101, 103)
    with open(infile) as f:
        lines = f.readlines()
        main(lines)

