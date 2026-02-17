from adventofcode.intcode import interpret_intcode


def main(inp):
    mem = list(map(int, inp.readline().rstrip().split(",")))
    print("Part 1: ", interpret_intcode(mem[::], stdin=[1]).stdout[0])
    print("Part 2: ", interpret_intcode(mem[::], stdin=[2]).stdout[0])


if __name__ == "__main__":
    import fileinput
    main(fileinput.input())

