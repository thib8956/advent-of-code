def reduce_polymer(p):
    res = [""]
    for x in p:
        if res[-1].swapcase() == x:
            res.pop()
        else:
            res.append(x)
    return "".join(res)


def main(inp):
    print("Part 1: ", len(reduce_polymer(inp)))
    letters = set(x.lower() for x in inp)
    min_ = 2 << 32
    for l in letters:
        p = inp.replace(l.lower(), "").replace(l.upper(), "")
        min_ = min(len(reduce_polymer(p)), min_)
    print("Part 2: ", min_)


if __name__ == "__main__":
    import fileinput
    inp = next(l.rstrip() for l in fileinput.input())
    main(inp)

