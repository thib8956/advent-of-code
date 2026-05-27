#!/usr/bin/env python3
import sys
from hashlib import md5
from multiprocessing import Process, Value


def solve(seed):
    needle = "0" * 5
    for i in range(900_000):
        hash = md5(seed + str(i).encode()).hexdigest()
        if hash.startswith(needle):
            # print(hash)
            return i
    assert False, "No solution found"


def worker(seed, start, step, stop_token, result):
    i = start
    while not stop_token.value:
        d = md5(seed + str(i).encode()).digest()
        if d[0] == 0 and d[1] == 0 and d[2] == 0:
            stop_token.value = 1
            result.value = i  # Store the result
            return
        i += step


def solve_parallel(seed):
    stop_token = Value("b", 0, lock=False)
    result = Value("i", -1)  # Default: -1 (no result yet)
    workers = []
    num_workers = 8
    for w in range(num_workers):
        p = Process(target=worker, args=(seed, w, num_workers, stop_token, result))
        p.start()
        workers.append(p)

    for p in workers:
        p.join()

    # Print the result
    if result.value != -1:
        return result.value
    else:
        assert False, "No solution found"


def main(inp):
    print("Part 1: ", solve(inp))
    print("Part 2: ", solve_parallel(inp))


if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else "file not found"
    with open(filename, "rb") as f:
        main(f.readline().rstrip())
