from itertools import pairwise


def is_safe(report):
    diffs = [b - a for a, b in pairwise(report)]
    return all(1 <= d <= 3 for d in diffs) or all(-3 <= d <= -1 for d in diffs)


def is_safe_with_problem_damper(report):
    for i, _ in enumerate(report):
        copy = report[::]
        del copy[i]
        if is_safe(copy):
            return True
    return False


def main(reports):
    safe_reports = sum(1 for x in reports if is_safe(x))
    print("Part 1: ", safe_reports)

    safe_reports = 0
    for report in reports:
        if is_safe_with_problem_damper(report):
            safe_reports += 1
    print("Part 2: ", safe_reports)


if __name__ == "__main__":
    import sys
    infile = sys.argv[1]
    with open(infile) as f:
        lines = f.readlines()
        lines = [list(map(int, x.rstrip().split())) for x in lines]
        main(lines)

