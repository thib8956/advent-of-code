#!/usr/bin/env python3
import fileinput
from collections import defaultdict


class Peekable:
    def __init__(self, lines):
        self.lines = lines
        self.pos = 0

    def peek(self):
        if self.pos < len(self.lines):
            return self.lines[self.pos]
        return None

    def next(self):
        self.pos += 1
        return self.lines[self.pos - 1]


def parse_tree(inp):
    "Parse input to adjacency list of files and directories"
    path = []
    adj = defaultdict(list)
    cmds = Peekable(inp)
    while cmds.pos < len(inp):
        line = cmds.next()
        if line.startswith("$ cd"):
            arg = line.removeprefix("$ cd ")
            if arg == "/":
                path = []
            elif arg == ".." and path:
                path.pop()
            else:
                path.append(arg)
        elif line.startswith("$ ls"):
            while (line := cmds.peek()) and not line.startswith("$"):
                line = cmds.next()
                if line.startswith("dir"):
                    name = line.removeprefix("dir ")
                    adj[tuple(path)].append(name)
                else:
                    size, name = line.split()
                    adj[tuple(path)].append((name, size))
    return adj


def calculate_sizes(adj):
    # DFS the tree to calculate size of each directory
    stack = [((), adj[()])]
    visited = {()}
    sizes = defaultdict(int)
    dirs = set()
    while stack:
        path, children = stack.pop()
        for child in children:
            if isinstance(child, tuple):  # file
                name, size = child
                sizes[path] += int(size)
                # print(f"file {name} {size}")
            else:  # dir
                child_path = (*path, child)
                # print(f"dir {child_path}")
                if child_path not in visited:
                    visited.add(child_path)
                    stack.append((child_path, adj[child_path]))
                    dirs.add(child_path)
    # Add up sizes of subdirectories to parent directories
    for path in sorted(dirs, key=len, reverse=True):
        if path:  # not root
            parent = path[:-1]
            sizes[parent] += sizes[path]
    return sizes


def part1(sizes):
    total = 0
    for size in sizes.values():
        if size <= 100000:
            total += size
    return total


def part2(sizes):
    total_space = sizes[()]  # size of root
    needed_space = 30000000 - (70000000 - total_space)
    candidates = [size for size in sizes.values() if size >= needed_space]
    return min(candidates)


def main(inp):
    adj = parse_tree(inp)
    sizes = calculate_sizes(adj)
    print("Part 1: ", part1(sizes))
    print("Part 2: ", part2(sizes))


if __name__ == "__main__":
    with fileinput.input() as f:
        lines = [x.rstrip() for x in f]
    main(lines)
