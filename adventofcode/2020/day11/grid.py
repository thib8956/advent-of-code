#!/usr/bin/env python3


class Grid:
    def __init__(self, inp):
        lines = inp.read().splitlines()
        self.cells = list("".join(lines))
        self.height = len(lines)
        self.width = len(lines[0])

    def __getitem__(self, key):
        x, y = key
        return cells[y * self.width + x]

    def __setitem__(self, key, value):
        x, y = key
        cells[y * self.width + x] = value

    def __iter__(self):
        return self.cells.__iter__()

    def __str__(self):
        "\n".join(
            "".join(
                grid[pos : pos + grid_width]
                for pos in range(0, self.width, self.height)
            )
        )
