import time
import math
import cmath
from itertools import combinations
from collections import defaultdict
from bisect import insort


def dist(a, b):
    "euclidean distance between two points (as complex numbers)"
    return abs(a - b)


def main(inp):
    asteroids = set()
    for y, l in enumerate(inp):
        for x, c in enumerate(l):
            if c == "#":
                asteroids.add(complex(x,y))
    base = part1(asteroids)
    #base = 22+28j

    # construct a list of asteroids for each angle, sorted by distance from the base
    angles = defaultdict(list)
    for a in asteroids:
        if a == base:
            continue
        angle = (math.degrees(cmath.phase(a - base)) + 90) % 360
        elt = (abs(a - base), a)
        insort(angles[angle], elt)

    i = 0
    for angle in sorted(angles):
        i += 1
        a = angles[angle].pop(0)
        if i == 200:
            _, a = a
            print("Part 2: ", int(a.real*100+a.imag))
            break


def part1(asteroids):
    """
    # ray cast solution not working
    start_time = time.perf_counter()
    sight = defaultdict(set)
    for a, b in combinations(asteroids, 2):
        if has_direct_sight_ray(a, b, asteroids):
            sight[a].add(b)
            sight[b].add(a)
    end_time = time.perf_counter() - start_time
    print(f"compute lines of sight ray {end_time:.4f}")
    m = max(sight.items(), key=lambda x: len(x[1]))
    print(m[0], len(m[1]))
    """
    #start_time = time.perf_counter()
    # construct line of sight for each asteroid
    sight = defaultdict(set)
    for a, b in combinations(asteroids, 2):
        if has_direct_sight(a, b, asteroids):
            sight[a].add(b)
            sight[b].add(a)
    #end_time = time.perf_counter() - start_time
    #print(f"compute lines of sight {end_time:.4f}")

    m = max(sight.items(), key=lambda x: len(x[1]))
    #print(m[0], len(m[1]))
    print("Part 1: ", len(m[1]))
    return m[0]


def has_direct_sight(a, c, asteroids):
    """
    Returns true if a can see c, i.e. they have no other asteroid between
    them. An asteroid b is between a and c if:
    dist(a,c) = dist(a,b) + dist(b,c).
    """
    ac = dist(a, c)
    eps = 0.00001  # avoid floating-point shenanigans
    for b in asteroids:  # check if any asteroid is blocking the view between a and c
        if b == a or b == c:
            continue
        if abs(dist(a, b) + dist(b, c) - ac) <= eps:
            return False
    return True


def has_direct_sight_ray(a, c, asteroids):
    # FIXME not working...
    """
    Cast a ray from a in the direction of c and return true if there is no
    obstacle between a and c
    """
    if c.real < a.real:
        a, c = c, a
    angle = cmath.phase(c - a)
    t = 0
    x = a.real
    y = a.imag
    while True:
        x = a.real + t * math.cos(angle)
        y = a.imag + t * math.sin(angle)
        t += 1
        if x >= c.real or y >= c.imag:
            return True
        if complex(int(x), int(y)) in asteroids:
            return False
    assert False, "Unreachable"


if __name__ == "__main__":
    import fileinput
    main(fileinput.input())

