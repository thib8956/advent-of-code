def part1(inp):
    horizontal_pos = 0
    depth = 0
    for line in inp:
        command, amount = line.split(" ")
        if command == "forward":
            horizontal_pos += int(amount)
        elif command == "up":
            depth -= int(amount)
        elif command == "down":
            depth += int(amount)
        #print(f"horizontal {horizontal_pos}, depth {depth}")
    print("Part 1", horizontal_pos * depth)


def part2(inp):
    horizontal_pos = 0
    depth = 0
    aim = 0
    for line in inp:
        command, amount = line.split(" ")
        if command == "forward":
            horizontal_pos += int(amount)
            # It increases your depth by your aim multiplied by X.
            depth += aim * int(amount)
        elif command == "up":
            aim -= int(amount)
        elif command == "down":
            aim += int(amount)
        #print(f"horizontal {horizontal_pos}, depth {depth}")
    print("Part 2", horizontal_pos * depth)


def main(input_file):
    with open(input_file) as f:
        entries = f.readlines()
        part1(entries)
        part2(entries)


if __name__ == "__main__":
    main("input.txt")
