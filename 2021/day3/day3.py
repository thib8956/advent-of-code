def calculate_gamma(inp):
    gamma_rate = [0] * len(inp[0])
    for line in inp:
        for index, char in enumerate(line):
            gamma_rate[index] += int(char)
    gamma_rate = [0 if x < len(inp) // 2 else 1 for x in gamma_rate]
    return gamma_rate


def part1(inp):
    gamma = calculate_gamma(inp)
    epsilon =  [0 if x == 1 else 1 for x in gamma]
    # power consumption = dec(gamma_rate) * dec(epsilon_rate)
    power = int("".join(str(x) for x in gamma), 2) * int("".join(str(x) for x in epsilon), 2)
    print("Part 1, power consumption : ", power)


def calculate_most_common(inp, pos):
    sum = 0
    for line in inp:
        sum += int(line[pos])
    return 0 if sum < len(inp) // 2 else 1


def filter_oxygen(inp, pos, most_common):
    result = []
    for line in inp:
        if int(line[pos]) == most_common:
            result.append(line)
    return result


def oxygen_rating(inp):
    result = inp[:]
    for pos in range(len(inp[0])):
        most_common = calculate_most_common(result, pos)
        result = filter_oxygen(result, pos, most_common)
        if len(result) == 1:
            return result


def co2_rating(inp):
    result = inp[:]
    for pos in range(len(inp[0])):
        least_common = 1 - calculate_most_common(result, pos)
        result = filter_oxygen(result, pos, least_common)
        if len(result) == 1:
            return result


def part2(inp):
    oxygen = oxygen_rating(inp)
    co2 = co2_rating(inp)
    res = int("".join(str(x) for x in oxygen), 2) * int("".join(str(x) for x in co2), 2)
    print(f"Part 2 : {res}")
        


def main(input_file):
    with open(input_file) as f:
        entries = [x.rstrip() for x in f.readlines()]
        part1(entries)
        part2(entries)


if __name__ == "__main__":
    main("input.txt")
