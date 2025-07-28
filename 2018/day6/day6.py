def dist(a, b):
    "manhattan distance"
    return abs(a.x - b.x) + abs(a.y - b.y)

def main(inp):
    pass


if __name__ == "__main__":
    import fileinput
    inp = list(l.rstrip() for l in fileinput.input())
    main(inp)

