from collections import defaultdict, namedtuple


Point = namedtuple('Point', ['x', 'y'])


def dist(a, b):
    "manhattan distance"
    return abs(a.x - b.x) + abs(a.y - b.y)


def iter_grid(bounds):
    min_, max_ = bounds
    for x in range(min_.x, max_.x + 1):
        for y in range(min_.y, max_.y + 1):
            yield Point(x, y)


def is_edge(p, bounds):
    start, end = bounds
    return p.x == start.x or p.x == end.x or p.y == start.y or p.y == end.y


def main(inp):
    grid = [Point(*map(int, l.split(", "))) for l in inp]
    bounds = (Point(min(p.x for p in grid), min(p.y for p in grid)),
              Point(max(p.x for p in grid), max(p.y for p in grid)))

    areas = defaultdict(int)
    infinite_regions = set()
    for p in iter_grid(bounds):
        # find dist to every point of grid
        distances = sorted((dist(p2, p), i) for i, p2 in enumerate(grid))
        # equally far from two or more coordinates, don't count
        if distances[0][0] == distances[1][0]:
            continue
        _, index = distances[0]
        areas[index] += 1
        if is_edge(p, bounds):
            infinite_regions.add(index)

    # remove all infinite regions by index
    for i in infinite_regions:
        del areas[i]
    print("Part 1: ", max(areas.values()))
    
    count = 0
    for cur in iter_grid(bounds):
        s = sum(dist(cur, p) for p in grid)
        if s < 10_000:
            count += 1
    print("Part 2: ", count)


if __name__ == "__main__":
    import fileinput
    inp = list(l.rstrip() for l in fileinput.input())
    main(inp)

