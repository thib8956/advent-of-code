import fileinput
import math


def step_simulation(positions, velocities):
    # update velocities by applying gravity (acceleration)
    for i in range(4):
        for j in range(i + 1, 4):
            for k in range(3):  # k for (x, y, z)
                if positions[i][k] < positions[j][k]:
                    velocities[i][k] += 1
                    velocities[j][k] -= 1
                elif positions[i][k] > positions[j][k]:
                    velocities[i][k] -= 1
                    velocities[j][k] += 1

    # update positions by applying velocity
    for pos, vel in zip(positions, velocities):
        pos[0] += vel[0]
        pos[1] += vel[1]
        pos[2] += vel[2]


def part1(positions, max_steps):
    velocities = [[0] * 3 for _ in range(4)]
    for _ in range(max_steps):
        step_simulation(positions, velocities)

    # compute energy for each star (potential + kinetic)
    total = 0
    for pos, vel in zip(positions, velocities):
        pot = sum(abs(x) for x in pos)
        kin = sum(abs(x) for x in vel)
        total += pot * kin

    return total


def part2(positions):
    initial_positions = [list(x) for x in positions]
    # find period_x, period_y, period_z: when back at initial pos + velocity is 0
    velocities = [[0] * 3 for _ in range(4)]
    periods = [None, None, None]  # [period_x, period_y, period_z]
    step = 0
    while step < 100000000:
        step_simulation(positions, velocities)

        # check periods
        for i in range(3):
            for j in range(4):
                if positions[j][i] != initial_positions[j][i] or velocities[j][i] != 0:
                    break
            else:  # all stars are back to initial position and velocity for axis i, so record period[i]
                if periods[i] is None:
                    periods[i] = step + 1

        step += 1
        if not None in periods: # we found the periods in steps for (x, y, z). return the result
            return math.lcm(*periods)
    assert False, "Max steps reached"


def main(inp):
    positions = []
    for line in inp:
        coords = list(map(int, (x.rstrip(">\n").split("=")[1] for x in line.split(", "))))
        positions.append(coords)
    print("Part 1: ", part1([list(x) for x in positions], 1000))
    print("Part 2: ", part2([list(x) for x in positions]))

if __name__ == '__main__':
    with fileinput.input() as f:
        main(f)
