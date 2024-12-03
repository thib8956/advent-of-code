def parse_part1(path):
    with open(path) as f:
        time, distance = f.readlines()
        time = [int(x) for x in time.split()[1:]]
        distance = [int(x) for x in distance.split()[1:]]
    return zip(time, distance)


def calculate_wins(data):
    total = 1
    for time, record in data:
        ways = 0
        for n in range(0, time+1):
            speed = n
            distance = (time-n) * speed
            if distance > record:
                ways += 1
        total *= ways
    return total


def parse_part2(path):
    with open(path) as f:
        time, distance = f.readlines()
        time = time.split(":")[1].replace(" ", "").rstrip()
        distance = distance.split(":")[1].replace(" ", "").rstrip()
        return int(time), int(distance)

if __name__ == "__main__":
    assert calculate_wins(zip(*[[7, 15, 30], [9, 40, 200]])) == 288  # part 1 example
    assert calculate_wins([[71530, 940200]]) == 71503  # part 2 example
    
    import sys
    if len(sys.argv) == 2:
        data = parse_part1(sys.argv[1])
        res = calculate_wins(data)
        print(f"Part 1, res={res}")
        data = parse_part2(sys.argv[1])
        res = calculate_wins([data])
        print(f"Part 2, res={res}")
