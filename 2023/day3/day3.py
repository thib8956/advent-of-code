from typing import Tuple, List, Set
from dataclasses import dataclass

@dataclass(frozen=True)
class Item:
    pos: Tuple[int, int]
    symbol: str


def browse_schema(schema):
    total_parts = 0
    buf = []
    max_row, max_col = len(schema), len(schema[0])

    symbols: List[Tuple[Item, Set[Item]]] = []
    numbers: List[Item] = []

    for y in range(max_row):
        for x in range(max_col):
            item = schema[y][x]
            if item.isnumeric():
                # continue parsing full number
                buf.append(item)
            else:
                neighbors = get_neighbors_of((x, y), schema)
                symbols.append((Item((x, y), item), set(neighbors)))
            if buf and not item.isnumeric():
                # end of a number, do the engine part check
                number = "".join(buf)
                neighbors = get_neighbors((x, y), len(buf), schema)
                start_pos = (x-len(number), y)
                symbols.append((Item((x, y), number), get_neighbors_of((x, y), schema)))
                numbers.append(Item(start_pos, number))
                
                if is_engine_part(neighbors):
                    total_parts += int(number)
                
                buf.clear()  # reached end of a number, clear buffer

    print(f"Part 1, sum of the parts numbers = {total_parts}")
    part2(symbols, numbers)

def part2(symbols, numbers):
    total_gears = 0
    stars = [(s, neighbors) for s, neighbors in symbols if s.symbol == "*"]
    for _, neighbors in stars:
        corresponding_numbers = set()
        digits = [n for n in neighbors if n.symbol.isdigit()]
        for digit in digits:
            # find full number (number.start_pos < digit.pos < number.end_pos)
            for number in numbers:
                if number.pos[1] - 1 <= digit.pos[1] <= number.pos[1] + 1 and number.pos[0] <= digit.pos[0] <= number.pos[0]+len(number.symbol):
                    corresponding_numbers.add(number.symbol)

        if len(corresponding_numbers) == 2:
            a, b = corresponding_numbers
            total_gears += int(a) * int(b)
            #print(f"star: {star.pos} {corresponding_numbers}")

    print(f"Part 2, sum of gear ratios = {total_gears}")
            


def is_engine_part(neighbors: List[Item]) -> bool:
    # get list of symbols (not '.', \n or a number)
    symbols = filter(lambda x: not x.symbol.isnumeric() and not x.symbol in (".", "\n"), neighbors)
    return next(symbols, None) is not None


def get_neighbors(pos: Tuple[int, int], length: int,  schema: List[List[str]]) -> List[Item]:
    x, y = pos
    start_x = x - length
    neighbors = [get_neighbors_of((x, y), schema) for x in range(start_x, x)]
    neighbors = [item for sublist in neighbors for item in sublist]  # flatten list of list
    return neighbors


def get_neighbors_of(pos: Tuple[int, int], schema: List[List[str]]) -> List[Item]:
    max_row, max_col = len(schema), len(schema[0])
    x, y = pos
    neighbors: List[Item] = []
    
    # top
    if y-1 >= 0:
        neighbors.append(Item((x, y-1), schema[y-1][x]))
    # bottom:
    if y+1 < max_row:
        neighbors.append(Item((x, y+1), schema[y+1][x]))
    # left
    if x-1 >= 0:
        neighbors.append(Item((x-1, y), schema[y][x-1]))
    # right
    if x+1 < max_col:
        neighbors.append(Item((x+1, y), schema[y][x+1]))
    # top-left
    if y-1 >= 0 and x-1 >= 0:
        neighbors.append(Item((x-1, y-1), schema[y-1][x-1]))
    # top-right
    if y-1 >= 0 and x+1 < max_col:
        neighbors.append(Item((x+1, y-1), schema[y-1][x+1]))
    # bottom-left
    if y+1 < max_row and x-1 >= 0:
        neighbors.append(Item((x-1, y+1), schema[y+1][x-1]))
    # bottom-right
    if y+1 < max_row and x+1 < max_col:
        neighbors.append(Item((x+1, y+1), schema[y+1][x+1]))

    return neighbors


if __name__ == "__main__":
    import sys
    infile = sys.argv[1]
    with open(infile) as f:
        schema = [[c for c in line] for line in f.readlines()]
        browse_schema(schema)
