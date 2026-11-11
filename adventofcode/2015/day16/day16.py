import fileinput
import re


def matches(traits, name, expected, part2=False):
    if name not in traits:
        return True
    if part2 and name in ("cats", "trees"):
        return traits[name] > expected
    if part2 and name in ("pomeranians", "goldfish"):
        return traits[name] < expected
    return traits[name] == expected


def find_sue(criteria, inp, part2=False):
    candidates = set(range(len(inp)))
    for name, expected in criteria:
        for i, traits in enumerate(inp):
            if i in candidates and not matches(traits, name, expected, part2):
                candidates.remove(i)
    return next(iter(candidates)) + 1

def main(inp):
    criteria = [
        ("children", 3), ("cats", 7), ("samoyeds", 2),
        ("pomeranians", 3), ("akitas", 0), ("vizslas", 0),
        ("goldfish", 5), ("trees", 3), ("cars", 2), ("perfumes", 1),
    ]
    parsed = []
    for line in inp:
        res = re.findall(r"(\w+):\s(\d+),?", line)
        parsed.append({ k: int(v) for k, v in res })
    print("Part 1: ", find_sue(criteria, parsed))
    print("Part 2: ", find_sue(criteria, parsed, True))


if __name__ == '__main__':
    with fileinput.input() as f:
        lines = [x.rstrip() for x in f]
    main(lines)
