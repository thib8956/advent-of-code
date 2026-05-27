#!/usr/bin/env python3
import fileinput
from sys import argv


def area(a, b):
    height = abs(a[1] - b[1]) + 1
    width = abs(a[0] - b[0]) + 1
    return height * width


def test_area():
    assert area((2, 5), (9, 7)) == 24, "Area between (2,5) and (9,7) should be 24"
    assert area((7, 1), (11, 7)) == 35, "Area between (7,1) and (11,7) should be 35"
    assert area((2, 5), (11, 1)) == 50, "Area between (2,5) and (11,1) should be 50"


def generate_ppm(inp, scale=100):
    """Generate a PPM file with scaled-down coordinates"""
    coords = [(x // scale, y // scale) for x, y in inp]

    max_x = max(x[0] for x in coords)
    min_x = min(x[0] for x in coords)
    max_y = max(x[1] for x in coords)
    min_y = min(x[1] for x in coords)

    height = max_y - min_y + 1
    width = max_x - min_x + 1

    print(f"Scaled dimensions: {width}x{height} (scale factor: {scale})")
    print(f"Original dimensions: {max(x[0] for x in inp)}x{max(x[1] for x in inp)}")

    arr = [[0] * (width) for _ in range(height)]
    for x, y in coords:
        if 0 <= y < height and 0 <= x < width:
            arr[y][x] = 1

    with open("test.ppm", "w") as f:
        f.write(f"P3\n{width} {height}\n255\n")
        for row in arr:
            for cell in row:
                f.write(f"{cell * 255} 0 0 ")
            f.write("\n")

    print("PPM file written to test.ppm")


def main(inp):
    coords = [tuple(map(int, x.split(","))) for x in inp]
    max_area = 0
    for a in coords:
        for b in coords:
            if a == b:
                continue
            max_area = max(max_area, area(a, b))
    print("Part 1:", max_area)


if __name__ == "__main__":
    lines = [x.rstrip() for x in fileinput.input()]
    # test_area()
    main(lines)
    # for vizualization
    # generate_ppm([tuple(map(int, x.split(","))) for x in lines])
