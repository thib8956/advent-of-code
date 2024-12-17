DIRECTIONS = {
    "^": 0 - 1j,  # up
    ">": 1 + 0j,  # right
    "v": 0 + 1j,  # down
    "<": -1 + 0j,  # left
}


def find_start_pos(grid):
    for y, row in enumerate(grid):
        for x, _ in enumerate(row):
            if grid[y][x] == "@":
                return complex(x, y)


def get_pos(grid, pos):
    x, y = int(pos.real), int(pos.imag)
    if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
        return grid[y][x]
    return None


def set_pos(grid, pos, val):
    x, y = int(pos.real), int(pos.imag)
    grid[y][x] = val


def debug_print(grid, move):
    print("Move ", move)
    for row in grid:
        print("".join(row))


def push(grid, pos, movement):
    direction = DIRECTIONS[movement]
    start_pos = pos + direction
    # Find the end pos of a consecutive "O" chain
    end_pos = start_pos
    while get_pos(grid, end_pos + direction) == "O":
        end_pos += direction
    if get_pos(grid, end_pos + direction) == ".":
        if movement == ">":
            start_x, end_x = int(start_pos.real), int(end_pos.real)
            y = int(start_pos.imag)
            for i in range(end_x, start_x - 1, -1):
                grid[y][i+1] = "O"  # shift "O" to the right
            grid[y][start_x] = "."
        elif movement == "<":
            start_x, end_x = int(start_pos.real), int(end_pos.real)
            y = int(start_pos.imag)
            for i in range(start_x, end_x + 1):
                grid[y][i+1] = "O"  # shift "O" to the left
            grid[y][start_x] = "."
        elif movement == "v":
            start_y, end_y = int(start_pos.imag), int(end_pos.imag)
            x = int(start_pos.real)
            for i in range(start_y, end_y + 1):
                grid[i+1][x] = "O"  # shift "O" down
            grid[start_y][x] = "."
        elif movement == "^":
            start_y, end_y = int(start_pos.imag), int(end_pos.imag)
            x = int(start_pos.real)
            for i in range(end_y, start_y - 1, -1):
                grid[i+1][x] = "O"  # shift "O" up
            grid[start_y][x] = "."


def main(content):
    grid, movements = content.split("\n\n")
    grid = [list(x) for x in grid.split("\n")]
    movements = movements.replace("\n", "")
    pos = find_start_pos(grid)

    for movement in movements:
        new_pos = pos + DIRECTIONS[movement]
        v = get_pos(grid, new_pos)
        match v:
            case ".":
                set_pos(grid, pos, ".")
                set_pos(grid, new_pos, "@")
                pos = new_pos
            case "O": 
                push(grid, pos, movement)
                if get_pos(grid, new_pos) == ".":
                    set_pos(grid, new_pos, "@")
                    set_pos(grid, pos, ".")
                    pos = new_pos
            case "#": pass
            case c: raise RuntimeError("This should never happen", c)
        debug_print(grid, movement)


if __name__ == "__main__":
    import sys
    infile = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
    with open(infile) as f:
        content = f.read()
        main(content)

