from dataclasses import dataclass
from collections import deque

@dataclass
class BingoItem:
    value: int
    marked: bool = False

def parse_grid(inp):
    raw_grid = [inp.popleft() for _ in range(5)]    
    grid = [[BingoItem(int(y)) for y in x.rstrip().split(" ") if y != ''] for x in raw_grid]
    return grid


def parse_grids(inp):
    grids = []
    while len(inp) >= 5:
        grid = parse_grid(inp)
        grids.append(grid)
        try:
            inp.popleft()
        except IndexError:
            break
    return grids

def check_line_win(grid):
    for line in grid:
        if all(n.marked for n in line): 
            return True
    return False


def check_column_win(grid):
    for col_number in range(len(grid[0])):
        column = [line[col_number] for line in grid]
        if all(x.marked for x in column):
            return True
    return False


def calculate_score(grid, final_num):
    unmarked = sum([sum([n.value for n in line if not n.marked]) for line in grid])
    return final_num * unmarked


def print_green(text, end):
    print(f"\033[1;32;40m{text}\033[0;37;40m", end=end)


def print_grid(grid):
    for line in grid:
        for col in line:
            if col.marked:
                print_green(f"{str(col.value).ljust(2)}", " ")
            else:
                print(f"{str(col.value).ljust(2)}", end=" ")
        print()
    print()


def play_bingo(numbers, grids):
    winning_grids = []
    for number in numbers:
        print(number)
        for grid in grids:
            for line in grid:
                for grid_number in line:
                    if grid_number.value == number:
                        grid_number.marked = True

        for grid in grids:
            win = [check_line_win(grid), check_column_win(grid)]
            if any(win):
                winning_grids.append((grid, number))
                # the grid won, remove it from the game
                grids.remove(grid)

    
    first_winning_grid, number = winning_grids[0]
    first_score = calculate_score(first_winning_grid, number)
    print(f"Part 1, score = {first_score}")

    last_winning_grid, number = winning_grids[-1]
    last_score = calculate_score(last_winning_grid, number)
    print(f"Part 2, score {last_score}")

def main(input_file):
    with open(input_file) as f:
        inp = deque(f.readlines())
    numbers = [int(x) for x in inp.popleft().split(",")]
    inp.popleft()
    grids = parse_grids(inp)
    play_bingo(numbers, grids)


if __name__ == "__main__":
    main("input.txt")
