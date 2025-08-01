# TODO replace PYTHONPATH hack with a proper solution, like making intcode an
# installed module https://stackoverflow.com/a/50194143
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).absolute().parent.parent / "intcode"))

from intcode import interpret_intcode, Interpreter


def main(inp):
    mem = list(map(int, inp.readline().rstrip().split(",")))
    print("Part 1: ", interpret_intcode(mem[::], stdin=[1]).stdout[0])
    print("Part 2: ", interpret_intcode(mem[::], stdin=[2]).stdout[0])


if __name__ == "__main__":
    import fileinput
    main(fileinput.input())

