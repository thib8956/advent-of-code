from math import prod


def part1(lines):
    result = set()
    for index, line in enumerate(lines):
        game_id = index + 1
        _, line = line.split(": ")
        result.add(int(game_id))
        hands = line.rstrip().split("; ")
        for hand in hands:
            colors = {"red": 0, "green": 0, "blue": 0}
            cubes = hand.split(", ")
            for cube in cubes:
                n, color = cube.split()
                colors[color] = int(n)
            if colors["red"] > 12 or colors["green"] > 13 or colors["blue"] > 14:
                # impossible configuration, remove this game_id from the result (if present)
                result.discard(int(game_id))
    print(f"Part 1: {sum(result)}")


def part2(lines):
    result = []
    for line in lines:
        colors = {"red": 0, "green": 0, "blue": 0}
        _, line = line.split(": ")
        hands = line.rstrip().split("; ")
        for hand in hands:
            cubes = hand.split(", ")
            for cube in cubes:
                n, color = cube.split()
                colors[color] = max(colors[color], int(n))
        result.append(prod(colors.values()))
    print(f"Part 2: {sum(result)}")
            

if __name__ == "__main__":
    import sys
    infile = sys.argv[1]
    with open(infile) as f:
        lines = f.readlines()
        part1(lines)
        part2(lines)
        
