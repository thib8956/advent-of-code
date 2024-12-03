from collections import OrderedDict

def part1(crabs):
    moves = OrderedDict()
    for pos in range(min(crabs), max(crabs) + 1):
        # calculate total fuel required to move to pos:
        for crab in crabs:
            fuel_cost = abs(pos - crab)
            moves[pos] = moves.get(pos, 0) + fuel_cost

    min_move = min(moves, key=moves.get)
    print(f"Part 1, min move {min_move}, cost {moves[min_move]}")

def part2(crabs):
    moves = OrderedDict()
    for pos in range(min(crabs), max(crabs) + 1):
        # calculate total fuel required to move to pos:
        for crab in crabs:
            dx = abs(pos - crab)
            # S = (n+1)(u0 + un)/2
            fuel_cost = dx * (dx+1)//2
            moves[pos] = moves.get(pos, 0) + fuel_cost

    min_move = min(moves, key=moves.get)
    print(f"Part 1, min move {min_move}, cost {moves[min_move]}")


if __name__ == "__main__":
    with open("input.txt") as infile:
        crabs = [int(x) for x in infile.readline().split(",")]
    part1(crabs)
    part2(crabs)

