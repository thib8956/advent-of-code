from collections import defaultdict


def path(graph, start, goal):
    path = []
    node = start
    while node != goal:
        node = graph[node]
        path.append(node)
    return path


def find_first_common(x, y):
    "returns the indices i and j of the first common element of x and y"
    for i, xx in enumerate(x):
        for j, yy in enumerate(y):
            if xx == yy:
                return i, j


def main(inp):
    graph = {}
    for l in inp:
        left, right = l.rstrip().split(")")
        graph[right] = left
    
    total = 0
    for node, child in graph.items():
        cnt = 1
        while child != "COM":
            child = graph[child]
            cnt += 1
        total += cnt
    print("Part 1: ", total)

    p1 = path(graph, "YOU", "COM")
    p2 = path(graph, "SAN", "COM")
    a, b = find_first_common(p1, p2)
    total_path = p1[:a] + p2[b::-1]  # p1 + p2 - p1 n p2
    print("Part 2: ", len(total_path) - 1)


if __name__ == "__main__":
    import fileinput
    main(fileinput.input())

