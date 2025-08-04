
def contains(first, second):
    "True if first ⊂ second or second ⊂ first"
    start_a, end_a = first
    start_b, end_b = second
    if start_b >= start_a and end_b <= end_a:
        return True
    start_a, end_a = second
    start_b, end_b = first
    if start_b >= start_a and end_b <= end_a:
        return True
    return False


def overlaps(first, second):
    start_a, end_a = first
    start_b, end_b = second
    if start_a <= start_b <= end_a:
        return True
    if start_b <= start_a <= end_b:
        return True
    return False


def main(content):
    total = 0
    for l in content:
        first, second = [tuple(map(int, x.split("-"))) for x in l.split(",")]
        if contains(first, second):
            total += 1
    print("Part 1: ", total)

    total = 0
    for l in content:
        first, second = [tuple(map(int, x.split("-"))) for x in l.split(",")]
        if overlaps(first, second):
            total += 1
    print("Part 2: ", total)



if __name__ == "__main__":
    import fileinput
    main([l.rstrip() for l in fileinput.input()])

