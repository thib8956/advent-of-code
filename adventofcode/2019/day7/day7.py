import sys
from pathlib import Path

sys.path.append(str(Path(__file__).absolute().parent.parent / "intcode"))

from itertools import cycle, permutations
from intcode import interpret_intcode, Interpreter

def main(inp):
    mem = list(map(int, inp.readline().rstrip().split(",")))
    max_ret = 0
    for seq in permutations([0, 1, 2, 3, 4], 5):
        ret = amplifiers(mem, list(seq))
        max_ret = max(ret.stdout[0], max_ret)
    print("Part 1: ", max_ret)

    max_ret = 0
    for seq in permutations((5, 6, 7, 8, 9)):
        ret = part2(mem, list(seq))
        max_ret = max(max_ret, ret)
    print("Part 2: ", max_ret)


def amplifiers(program, sequence):
    ret = interpret_intcode(program[::], [sequence.pop(0), 0])
    ret = interpret_intcode(program[::], [sequence.pop(0), ret.stdout.pop()])
    ret = interpret_intcode(program[::], [sequence.pop(0), ret.stdout.pop()])
    ret = interpret_intcode(program[::], [sequence.pop(0), ret.stdout.pop()])
    ret = interpret_intcode(program[::], [sequence.pop(0), ret.stdout.pop()])
    return ret


def part2(program, sequence):
    amplifiers = [Interpreter(program[::], [sequence.pop(0)]) for _ in range(5)]
    it = cycle(enumerate(amplifiers))

    id_, amp = next(it)
    inp = 0
    max_signal = 0
    while True:
        max_signal = max(max_signal, inp)
        amp.stdin.append(inp)
        amp.interpret()
        out = amp.stdout
        if amp.halted:
            break
        next_id, next_amp = next(it)
        inp = out.pop(0)
        amp = next_amp
        id_= next_id
    return max_signal


def tests():
    program = [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]
    sequence = [4, 3, 2, 1, 0]
    res = amplifiers(program, sequence)
    assert res.stdout == [43210]

    program = [3,23,3,24,1002,24,10,24,1002,23,-1,23,
               101,5,23,23,1,24,23,23,4,23,99,0,0]
    sequence = [0,1,2,3,4]
    res = amplifiers(program, sequence)
    assert res.stdout == [54321]


    program = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
               1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
    sequence = [1,0,4,3,2]
    res = amplifiers(program, sequence)
    assert res.stdout == [65210]


def tests2():
    program = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
               27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
    sequence = [9,8,7,6,5]
    assert part2(program, sequence) == 139629729


    program = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
               -5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
               53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
    sequence = [9,7,8,5,6]
    assert part2(program, sequence) == 18216


if __name__ == "__main__":
    import fileinput
    tests()
    tests2()
    main(fileinput.input())

