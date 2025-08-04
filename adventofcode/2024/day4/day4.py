DIRECTIONS = (
    (0, -1),   # N
    (-1, -1),  # NW
    (1, -1),   # NE
    (-1, 0),   # W
    (1, 0),    # E
    (0, 1),    # S
    (-1, 1),   # SW
    (1, 1),    # SE
)

def get_grid_pos(grid, pos):
    x, y = pos
    if 0 <= x < len(grid):
        if 0 <= y < len(grid[0]):
            return grid[y][x]
    return None


def part1(grid):
    count = 0
    for y, row in enumerate(grid):
        for x, letter in enumerate(row):
            if letter != "X":
                continue
            for direction in DIRECTIONS:
                acc = letter
                for i in range(1, 4):
                    dx, dy = direction
                    pos = (x + i*dx, y + i*dy)
                    next_letter = get_grid_pos(grid, pos)
                    if next_letter is not None:
                        acc += next_letter
                    else:
                        break  # out-of-bounds, go to next direction
                if acc == "XMAS":
                    count += 1
    print("Part 1: ", count)


def part2(grid):
    count = 0
    for y, row in enumerate(grid):
        for x, _ in enumerate(row):
            if y + 2 >= len(grid) or x + 2 >= len(grid[0]):
                continue
            if grid[y+1][x+1] != "A":  # center letter is always "A"
                continue
            # M.S / .A. / M.S
            if grid[y][x] == "M" and grid[y][x+2] == "S" and grid[y+2][x] == "M" and grid[y+2][x+2] == "S":
                count += 1
            # M.M / .A. / S.S
            if grid[y][x] == "M" and grid[y][x+2] == "M" and grid[y+2][x] == "S" and grid[y+2][x+2] == "S":
                count += 1
            # S.M / .A. / S.M
            if grid[y][x] == "S" and grid[y][x+2] == "M" and grid[y+2][x] == "S" and grid[y+2][x+2] == "M":
                count += 1
            # S.S / .A. / M.M
            if grid[y][x] == "S" and grid[y][x+2] == "S" and grid[y+2][x] == "M" and grid[y+2][x+2] == "M":
                count += 1
    print("Part 2: ", count)



if __name__ == "__main__":
    import sys
    infile = sys.argv[1] if 1 < len(sys.argv) else "example.txt"
    with open(infile) as f:
        grid = [l.rstrip() for l in f.readlines()]
        part1(grid)
        part2(grid)

