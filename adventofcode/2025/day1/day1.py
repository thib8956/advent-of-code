def part1(lines):
    pos = 50
    cnt = 0
    for rotation in lines:
        direction = -1 if rotation[0] == "L" else 1
        amount = int(rotation[1:])
        pos = (pos + amount * direction) % 100
        if pos == 0:
            cnt += 1
    print("Part 1: ", cnt)



def part2(lines):
    pos = 50
    cnt = 0
    for rotation in lines:
        direction = -1 if rotation[0] == "L" else 1
        amount = int(rotation[1:])
        pos0 = pos % 100
        # k0  is the smallest positive number of clicks (1..100) after the
        # start of the current rotation at which the dial first reaches
        # position 0.
        k0 = ((100 - pos0) % 100) if direction == 1 else (pos0 % 100)
        if k0 == 0:
            k0 = 100
        if amount >= k0:
            cnt += 1 + (amount - k0) // 100
        pos = (pos + direction * amount) % 100
        print(rotation, pos, cnt)
    print("Part 2: ", cnt)


if __name__ == "__main__":
    import sys
    infile = sys.argv[1]
    
    with open(infile) as f:
        lines = f.readlines()
        lines = [x.rstrip() for x in lines]
        part1(lines)
        part2(lines)

