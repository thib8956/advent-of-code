def check_slope_for_trees(plan, x_right=3, y_down=1):
    x_max = len(plan[0])
    y_max = len(plan)
    
    x, y = 0, 0
    tree_count = 0
    while y < y_max - 1:
        x += x_right
        x %= x_max  # wrap x
        y += y_down

        pos = plan[y][x]
        if pos == '#':
            tree_count += 1
    return tree_count


def part1(inp):
    plan = [line.rstrip() for line in open(inp)]
    tree_count = check_slope_for_trees(plan)
    print(f"number of trees : {tree_count}")


def part2(inp):
    plan = [line.rstrip() for line in open(inp)]
    slopes = [{"x": 1, "y": 1}, {"x": 3, "y": 1}, {"x": 5, "y": 1}, {"x": 7, "y": 1}, {"x": 1, "y": 2}]
    tree_product = 1
    for slope in slopes:
        tree_count = check_slope_for_trees(plan, slope["x"], slope["y"])
        tree_product *= tree_count
        print(f"slope {slope} number of trees : {tree_count}")
        print(f"Cumulative product of tress : {tree_product}")

if __name__ == "__main__":
    part1('input.txt')
    part2('input.txt')
