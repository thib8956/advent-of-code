import re
import math
from itertools import cycle

def parse_input(infile):
    with open(infile) as f:
        content = f.read().rstrip()
        directions, nodes = content.split("\n\n")
        directions = directions.strip()
        nodes = nodes.split("\n")
        nodes = [n.split(" = ") for n in nodes]
        nodes = {k: re.findall(r"\w{3}", v) for k, v in nodes}
        return directions, nodes


def part1(directions, nodes):
    iterations = 0
    current_node = "AAA"
    for d in cycle(directions):
        if current_node == "ZZZ":
            break
        iterations += 1
        if d == "L":
            current_node = nodes[current_node][0]
        else:
            current_node = nodes[current_node][1]
    print(f"Part 1: reached 'ZZZ' in {iterations} iterations")


def part2(directions, nodes):
    current_nodes = [k for k in nodes.keys() if k.endswith("A")]
    # keep track of iterations number for each visited node 
    # (the number will stop to beeing incremented once the node n_i value reached the target value 'xxZ')
    iterations = [0] * len(current_nodes)

    for d in cycle(directions):
        if all(c.endswith("Z") for c in current_nodes):
            break

        if d == "L":
            new_nodes = []
            for i, n in enumerate(current_nodes):
                if n.endswith("Z"):  # end condition already reached for this node
                    new_nodes.append(n)
                else:
                    new_nodes.append(nodes[n][0])
                    iterations[i] += 1
            current_nodes = new_nodes
        else:
            new_nodes = []
            for i, n in enumerate(current_nodes):
                if n.endswith("Z"):  # end condition already reached for this node
                    new_nodes.append(n)
                else:
                    new_nodes.append(nodes[n][1])
                    iterations[i] += 1
            current_nodes = new_nodes

    # the result is the lowest common multiple between the number of iterations
    # for each node
    result = math.lcm(*iterations)
    print(f"Part 2: reached all nodes such that 'xxZ' in {result} iterations")


if __name__ == "__main__":
    import sys
    import os
    SCRIPTPATH = os.path.dirname(os.path.realpath(__file__))
    infile = sys.argv[1] if len(sys.argv) == 2 else "example.txt"

    directions, nodes = parse_input(os.path.join(SCRIPTPATH, infile))
    part1(directions, nodes)

    directions, nodes = parse_input(os.path.join(SCRIPTPATH, infile))
    part2(directions, nodes)
