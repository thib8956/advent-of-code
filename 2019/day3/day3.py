#!/usr/bin/env python3


def manhattan_distance(p):
    return abs(p[0]) + abs(p[1])


def points_for_wire(wire):
    x, y, count = 0, 0, 0
    points = {}
    # (x, y)
    directions = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
    for p in wire:
        # D42 -> for _ in range(42)
        for _ in range(int(p[1:])):
            offset = directions[p[0]]
            x += offset[0]
            y += offset[1]
            count += 1
            points[(x ,y)] = count

    return points


def find_min_distance(wire1, wire2):
    points1 = points_for_wire(wire1)
    points2 = points_for_wire(wire2)

    intersections = points1.keys() & points2.keys()
    closest = min((intersection for intersection in intersections), key=manhattan_distance)

    return manhattan_distance(closest)


def find_least_steps(wire1, wire2):
    points1 = points_for_wire(wire1)
    points2 = points_for_wire(wire2)

    intersections = points1.keys() & points2.keys()
    # Intersection with the least steps
    least_steps = min(intersections, key=lambda x: points1[x] + points2[x])

    return points1[least_steps] + points2[least_steps]


def tests():
    inputs = (
        (("R8", "U5", "L5", "D3"), ("U7", "R6", "D4", "L4")),
        (("R75","D30","R83", "U83", "L12", "D49", "R71", "U7", "L72"), ("U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83")),
        (("R98", "U47", "R26", "D63", "R33", "U87", "L62", "D20", "R33", "U53", "R51"), ("U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"))
    )

    # Part 1
    expected = (6, 159, 135)
    for i, inp in enumerate(inputs):
        result = find_min_distance(inp[0], inp[1])
        assert result == expected[i], "Result for {} should be {}, was {}".format(
            inp, expected[i], result
        )
    
    # Part 2
    # expected number of steps
    expected_part2 = (30, 610, 410)
    print("All tests passed.")
    for i, inp in enumerate(inputs):
        result = find_least_steps(inp[0], inp[1])
        assert result == expected_part2[i], "Result for {} should be {}, was {}".format(
            inp, expected_part2[i], result
        )

if __name__ == "__main__":
    tests()
    import sys
    infile = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
    with open(infile) as raw_input:
        lines = raw_input.readlines()
        wire1, wire2 = [line.strip("\n").split(",") for line in lines]
        print("Part 1 -- distance = ", find_min_distance(wire1, wire2))
        print("Part 2 -- steps = ", find_least_steps(wire1, wire2))
