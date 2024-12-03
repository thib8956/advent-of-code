#! /usr/bin/env python3


def calculate_fuel_iterative(mass):
    total = 0
    new_mass = mass
    while True:
        new_mass = new_mass // 3 - 2
        if new_mass < 0:
            break
        total += new_mass
    return total


def calculate_total_fuel_mass(input_file, mass_function=lambda x: x // 3 - 2):
    total = 0
    with open(input_file) as masses:
        for mass in masses:
            total += mass_function(int(mass))
    return total


def test_part2():
    inputs = (14, 1969, 100756)
    expected = (2, 966, 50346)
    for i, inp in enumerate(inputs):
        result = calculate_fuel_iterative(inp)
        assert result == expected[i], "Result for {} should be {}, was {}".format(
            inp, expected[i], result
        )
    print("All tests passed for part 2.")


if __name__ == "__main__":
    print("Part 1 - total mass: ", calculate_total_fuel_mass("./input.txt"))

    test_part2()
    print(
        "Part 2 -- total mass: ",
        calculate_total_fuel_mass("./input.txt", calculate_fuel_iterative),
    )
