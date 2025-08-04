from itertools import zip_longest


def grouper(n, iterable):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args)


def part1(sections):
    # consume seed section
    _, seeds = next(sections)
    seeds = [int(s) for s in seeds]
    for _, mapping in sections:
        seeds = [apply_mapping(s, mapping) for s in seeds]
    print(f"Part 1, lowest location number = {min(seeds)}")


def part2(sections):
    # consume seed section
    _, seeds = next(sections)
    seeds = [int(s) for s in seeds]

    min_seed = 2**128
    for start_seed, length in grouper(2, seeds):
        subseeds = range(start_seed, start_seed + length)
        print(f"calculate_for_subseeds(subseeds len={len(subseeds)})")
        res = calculate_for_subseeds(subseeds, sections)
        mini = min(res)
        if mini < min_seed:
            min_seed = mini
    
    print(f"Part 2 {min_seed}")


def calculate_for_subseeds(seeds, sections):
    new_seeds = seeds
    for _, mapping in sections:
        new_seeds = [apply_mapping(s, mapping) for s in new_seeds]
    return new_seeds


def apply_mapping(seed, mapping):
    for dst, src, length in grouper(3, mapping):
        src, length, dst = int(src), int(length), int(dst)
        end = src + length
        if src <= seed < end:
            return seed + (dst-src)
    return seed


def parse_input(infile):
    with open(infile) as f:
        sections = f.read().split("\n\n")
        sections = ((title, numbers) for title, numbers in (s.split(":") for s in sections))
        sections = ((title, numbers.split()) for title, numbers in sections)
        return sections


if __name__ == "__main__":
    import sys
    import os
    SCRIPTPATH = os.path.dirname(os.path.realpath(__file__))

    infile = next(iter(sys.argv[1:]), None)
    sections = parse_input(infile or os.path.join(SCRIPTPATH, "example.txt"))
    part1(sections)
    sections = parse_input(infile or os.path.join(SCRIPTPATH, "example.txt"))
    part2(sections)

