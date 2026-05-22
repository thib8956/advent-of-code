#!/usr/bin/env python3
import fileinput


def main(inp):
    start_pos = None
    splitters = set()
    x, y = 0, 0
    for y, row in enumerate(inp):
        for x, ch in enumerate(row):
            if ch == "S":
                start_pos = x, y
            elif ch == "^":
                splitters.add((x, y))

    part1(start_pos, splitters, max_y=y)
    part2(start_pos, splitters, x, max_y=y)


def part1(pos, splitters, max_y):
    "BFS the grid and count the splitters"
    queue = [pos]
    visited = set()
    splitter_cnt = 0
    while True:
        current_pos = queue.pop(0)
        visited.add(current_pos)
        new_pos = current_pos[0], current_pos[1] + 1
        if new_pos in visited:
            continue
        if new_pos[1] > max_y:
            break
        if new_pos in splitters:
            visited.add(new_pos)
            splitter_cnt += 1
            split_left_pos = new_pos[0] - 1, new_pos[1]
            split_right_pos = new_pos[0] + 1, new_pos[1]
            if split_left_pos not in visited:
                queue.append(split_left_pos)
            if split_right_pos not in visited:
                queue.append(split_right_pos)
        else:
            queue.append(new_pos)
    print("Part 1: ", splitter_cnt)


def part2(start_pos, splitters, max_x, max_y):
    # store the number of timelines at each position
    current_row = [0] * (max_x + 1)
    current_row[start_pos[0]] = 1  # set start pos in the first row
    for y in range(max_y):
        new_row = [0] * (max_x + 1)
        for i, cnt in enumerate(current_row):
            if cnt > 0:
                new_pos = i, y + 1
                if new_pos in splitters:
                    new_row[i - 1] += cnt
                    new_row[i + 1] += cnt
                else:
                    new_row[i] += cnt
        current_row = new_row
    print("Part 2: ", sum(current_row))


if __name__ == "__main__":
    lines = [x.rstrip() for x in fileinput.input()]
    main(lines)
