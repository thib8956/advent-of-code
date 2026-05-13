#!/usr/bin/env python3

import json
import re
from collections import deque


def main(inp):
    total = sum(map(int, re.findall(r"(-?\d+)", inp)))
    print("Part 1: ", total)
    root = json.loads(inp)
    print("Part 2: ", bfs(root))


def bfs(json_data):
    """
    BFS on the json data and sum all the numbers. If a node contains the value
    "red", we skip it and all its children
    """
    queue = deque([(json_data, "")])  # (node, path)
    visited = set()
    total = 0
    while queue:
        node, path = queue.popleft()
        if path not in visited:
            visited.add(path)
            if isinstance(node, int):
                total += node
            elif isinstance(node, dict):
                has_red = "red" in node.values()
                if not has_red:
                    for key, child in node.items():
                        queue.append((child, f"{path}.{key}"))
            elif isinstance(node, list):
                for idx, child in enumerate(node):
                    queue.append((child, f"{path}[{idx}]"))
    return total


if __name__ == "__main__":
    import fileinput

    line = next(fileinput.input()).rstrip()
    main(line)
