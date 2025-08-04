from collections import defaultdict

def main(infile):
    points = defaultdict(int)
    with open(infile) as f:
        for line in f:
            start, end = line.split(" -> ")
            start_x, start_y = [int(x) for x in start.split(",")]
            end_x, end_y = [int(x) for x in end.split(",")]

            # column |
            if start_x == end_x:
                step = 1 if start_y < end_y else -1
                for y in range(start_y, end_y + step, step):
                    points[(start_x, y)] = points[(start_x, y)] + 1
            # line -
            elif start_y == end_y:
                step = 1 if start_x < end_x else -1
                for x in range(start_x, end_x + step, step):
                    points[(x, start_y)] = points[(x, start_y)] + 1
            # diagonal \
            elif ((start_x < end_x and start_y > end_y) 
                    or (start_x > end_x and start_y < end_y)):
                step = 1 if start_y > end_y else -1
                for dx in range(0, end_x - start_x + step, step):
                    points[(start_x + dx, start_y - dx)] = points[(start_x + dx, start_y + dx)] + 1
            # diagonal /
            elif ((start_x < end_x and start_y < end_y)
                    or (start_x > end_x and start_y > end_y)):
                step = 1 if start_y < end_y else -1
                for dx in range(0, end_x - start_x + step, step):
                    points[(start_x + dx, start_y + dx)] = points[(start_x + dx, start_y + dx)] + 1
                    
    res = len([x for x in points.values() if x >= 2])
    print(res)


if __name__ == "__main__":
    import sys
    infile = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
    main(infile)
