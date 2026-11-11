import fileinput


def solve(containers, target=150):
    "This is knapsack problem. Count the number of ways to sum to target using a recursive approach and pruning."
    containers.sort(reverse=True)

    min_used_containers = [99, 0]  # number of containers, number of ways
    def rec(i=0, current_sum=0, used=0):
        # base case
        if i == len(containers):
            if current_sum == target:
                if used < min_used_containers[0]:
                    min_used_containers[0] = used
                    min_used_containers[1] = 1
                elif used == min_used_containers[0]:
                    min_used_containers[1] += 1
                return 1
            else:
                return 0
        n = 0
        # All values are positive, so adding can only increase the sum. If the current sum overshoots, we can prune the branch
        if current_sum + containers[i] <= target:
            n += rec(i + 1, current_sum + containers[i], used + 1)  # pick
        n += rec(i + 1, current_sum, used)  # don't pick
        return n

    # returns the number of ways to sum to target and the number of ways to sum to target using the minimum number of containers
    return rec(), min_used_containers[1]


def main(inp):
    containers = [int(x) for x in inp]
    part1, part2 = solve(containers)
    print("Part 1: ", part1)
    print("Part 2: ", part2)


if __name__ == "__main__":
    with fileinput.input() as f:
        lines = [x.rstrip() for x in f]
    main(lines)
