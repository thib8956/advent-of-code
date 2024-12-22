from itertools import combinations


def in_bounds(pos, grid):
    x, y = int(pos.real), int(pos.imag)
    if 0 <= y < len(grid) and 0 <= x < len(grid[0]):
        return True
    return False


def part1(locations, grid):
    antinodes = set()
    for first, second in combinations(locations.items(), 2):
        first_loc, first_freq = first
        second_loc, second_freq = second
        if first_freq == second_freq:
            slope = first_loc - second_loc
            a = first_loc + slope
            if in_bounds(a, grid):
                antinodes.add(a)
            b = second_loc - slope
            if in_bounds(b, grid):
                antinodes.add(b)
    return antinodes


def part2(locations, grid):
    antinodes = set()
    for first, second in combinations(locations.items(), 2):
        first_loc, first_freq = first
        second_loc, second_freq = second
        antinodes.update([first_loc, second_loc])
        if first_freq == second_freq:
            slope = first_loc - second_loc
            i = 1
            while True:
                a = first_loc + i*slope
                if not in_bounds(a, grid):
                    break
                antinodes.add(a)
                i += 1
            j = 0
            while True:
                b = second_loc - j*slope
                if not in_bounds(b, grid):
                    break
                antinodes.add(b)
                j += 1
    return antinodes


def main(lines):
    grid = [l.rstrip() for l in lines]
    locations = {}

    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c != '.':
                locations[complex(x, y)] = c

    print("Part 1: ", len(part1(locations, grid)))
    print("Part 2: ", len(part2(locations, grid)))



if __name__ == "__main__":
    import sys
    infile = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
    with open(infile) as f:
        main(f.readlines())

