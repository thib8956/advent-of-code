import sys
from pathlib import Path

# TODO replace PYTHONPATH hack with a proper solution, like making intcode an
# installed module https://stackoverflow.com/a/50194143
sys.path.append(str(Path(__file__).absolute().parent.parent / "intcode"))

import itertools
from intcode import interpret_intcode


def main(inp):
    mem = list(map(int, inp.readline().rstrip().split(",")))
    max_ret = 0
    for seq in itertools.permutations([0, 1, 2, 3, 4], 5):
        ret = amplifiers(mem, list(seq))
        #print(ret)
        max_ret = max(ret[0], max_ret)
    print(max_ret)


def amplifiers(program, sequence):
    ret = interpret_intcode(program[::], [sequence.pop(0), 0])
    ret = interpret_intcode(program[::], [sequence.pop(0), ret.pop()])
    ret = interpret_intcode(program[::], [sequence.pop(0), ret.pop()])
    ret = interpret_intcode(program[::], [sequence.pop(0), ret.pop()])
    ret = interpret_intcode(program[::], [sequence.pop(0), ret.pop()])
    return ret

def tests():
    program = [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]
    sequence = [4, 3, 2, 1, 0]
    res = amplifiers(program, sequence)
    assert res == [43210]

    program = [3,23,3,24,1002,24,10,24,1002,23,-1,23, 101,5,23,23,1,24,23,23,4,23,99,0,0]
    sequence = [0,1,2,3,4]
    res = amplifiers(program, sequence)
    assert res == [54321]


    program = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33, 1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
    sequence = [1,0,4,3,2]
    res = amplifiers(program, sequence)
    assert res == [65210]

    print("All tests passed")

if __name__ == "__main__":
    import fileinput
    main(fileinput.input())
    tests()

