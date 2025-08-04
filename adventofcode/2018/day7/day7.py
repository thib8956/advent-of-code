#!/usr/bin/env python3
import re
from bisect import insort
from collections import defaultdict


def topological_sort(graph, reverse_deps):
    # find starting nodes: with no incoming edges (aka indegree 0)
    queue = sorted([task for task in graph.keys() if reverse_deps[task] == set()])
    order = []
    seen = set()
    while queue != []:
        current = queue.pop(0)
        if current not in seen:
            seen.add(current)
            order.append(current)
            # add dependencies if all prerequisites are already visited,
            # insert them in alphabetical order
            for d in graph[current]:
                if all(x in order for x in reverse_deps[d]):
                    insort(queue, d)
    return order


def main(inp):
    dependencies = defaultdict(set)
    reverse_deps = defaultdict(set)
    for l in inp:
        first, second = re.findall(r"[sS]tep (\w)", l)
        dependencies[first].add(second)
        reverse_deps[second].add(first)

    order = topological_sort(dependencies, reverse_deps)
    print("Part 1: ", "".join(order))


    done = []
    doing = dict()

    workers = 5
    step = 0
    number_of_tasks = len(order)
    while len(done) != number_of_tasks:
        assert len(doing) <= workers
        for i in range(workers):
            # check if the worker has a pending task
            if i in doing:
                task = doing[i]
                if is_task_done(task, step):
                    #print(f"{step}: worker #{i}, task {task} done")
                    del doing[i]
                    done.append(task[0])
                else:
                    continue
            next_task = get_task(dependencies, reverse_deps, done, doing)
            if next_task is not None:
                #print(f"{step}: worker #{i}, starting task {next_task}")
                doing[i] = (next_task, step)
        #print(f"{step}: {doing} {done}")
        if len(done) == number_of_tasks:
            break
        step += 1
        print(f"{step}\t{'\t'.join(x[0] for x in doing.values())}")
    print(step)

def get_task(graph, reverse_deps, done, doing):
    queue = sorted([task for task in graph.keys() if all(x in done for x in reverse_deps[task])])
    doingg = [x[0] for x in doing.values()]
    for t in queue:
        if t not in done and t not in doingg:
            return t
    return None


def is_task_done(task, step):
    letter, start_t = task
    duration = ord(letter) - ord("A") + 61
    if step - start_t >= duration:
        return True
    return False


if __name__ == '__main__':
    import sys
    infile = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
    with open(infile) as inp:
        main([l.rstrip() for l in inp.readlines()])

