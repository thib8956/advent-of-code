#!/usr/bin/env python3
import fileinput
import re
from dataclasses import dataclass


@dataclass
class Reeinder:
    name: str
    speed: int
    duration: int
    rest_duration: int
    cnt: int = 0
    total_distance: int = 0
    is_flying: bool = True
    score = 0

    def __post_init__(self):
        self.cnt = self.duration


def main(inp):
    data = {x.split()[0]: tuple(map(int, re.findall(r"(\d+)", x))) for x in inp}
    simulation = [
        Reeinder(name, speed, duration, rest_duration)
        for name, (speed, duration, rest_duration) in data.items()
    ]
    max_steps = 2503
    for _ in range(max_steps):
        for reeinder in simulation:
            if reeinder.is_flying:
                reeinder.total_distance += reeinder.speed
                reeinder.cnt -= 1
                if reeinder.cnt == 0:
                    reeinder.is_flying = False
                    reeinder.cnt = reeinder.rest_duration
            else:
                reeinder.cnt -= 1
                if reeinder.cnt == 0:
                    reeinder.is_flying = True
                    reeinder.cnt = reeinder.duration
        # for part 2, score the first reeinder at each simulation step
        max_dist = max(x.total_distance for x in simulation)
        for reeinder in simulation:
            if reeinder.total_distance == max_dist:
                reeinder.score += 1

    print("Part 1:", max(x.total_distance for x in simulation))
    print("Part 2:", max(x.score for x in simulation))


if __name__ == "__main__":
    lines = [x.rstrip() for x in fileinput.input()]
    main(lines)
