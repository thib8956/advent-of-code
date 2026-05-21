import time


def generate_invalid_ids(max_half_len):
    res = []
    for n in range(1, max_half_len):
        for prefix in range(10 ** (n - 1), 10**n):
            res.append(prefix * (10**n + 1))
    return sorted(res)


def generate_invalid_ids_part2():
    invalids = set()
    for n in range(1, 100000):
        n_str = str(n)
        length = len(n_str)
        if 1 <= length <= 5:
            max_k = 10 // length
            for k in range(2, max_k + 1):
                repeated = int(n_str * k)
                invalids.add(repeated)
    return sorted(invalids)


def main(content):
    t0 = time.perf_counter_ns()

    pairs = content.split(",")
    pairs = [tuple(map(int, x.split("-"))) for x in pairs]
    t1 = time.perf_counter_ns()

    parsing_ms = (t1 - t0) / 1_000_000
    print(f"Parsing took {parsing_ms:.4f} ms")

    max_len = max(len(str(pair[1])) for pair in pairs)
    invalid_ids = generate_invalid_ids(max_half_len=max_len // 2 + 1)
    t2 = time.perf_counter_ns()

    gen1_ms = (t2 - t1) / 1_000_000
    print(f"Generating invalid ids took {gen1_ms:.3f} ms")

    invalid_ids_part2 = generate_invalid_ids_part2()
    t3 = time.perf_counter_ns()

    gen2_ms = (t3 - t2) / 1_000_000
    print(f"Generating invalid ids for part 2 took {gen2_ms:.3f} ms")

    total = 0
    total_part2 = 0
    for pair in pairs:
        start, end = pair
        for n in invalid_ids:
            if start <= n <= end:
                total += n
            if n > end:
                break
        for n in invalid_ids_part2:
            if start <= n <= end:
                total_part2 += n
            if n > end:
                break
    t4 = time.perf_counter_ns()

    loop_ms = (t4 - t3) / 1_000_000
    print(f"Looping took {loop_ms:.3f} ms")
    print("Part 1: ", total)
    print("Part 2: ", total_part2)


if __name__ == "__main__":
    import sys

    infile = sys.argv[1]

    with open(infile) as f:
        content = f.read().rstrip()
        main(content)
