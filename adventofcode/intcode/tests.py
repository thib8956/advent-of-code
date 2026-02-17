# Run with pytest
import logging
from intcode import *


def run_test(program, expected_mem=None, stdin=[], expected_out=None):
    mem = program[::]
    out = interpret_intcode(mem, stdin=stdin)
    if expected_mem is not None:
        assert expected_mem == out.memory
    if expected_out is not None:
        assert expected_out == out.stdout


def test_day2():
    tests = [
        [[1,0,0,0,99], [2,0,0,0,99]],  # ADD 1 + 1 to location 0
        [[2,3,0,3,99], [2,3,0,6,99]],  # MUL 2 * 3 to location 3
        [[2,4,4,5,99,0], [2,4,4,5,99,9801]],  # MUL 99 * 99 to location 5 (9801)
        [[1,1,1,4,99,5,6,0,99], [30,1,1,4,2,5,6,0,99]],
    ]
    for program, expected in tests:
        run_test(program, expected)


def test_day5_basic():
    # Using position mode, consider whether the input is equal to 8; output 1
    # (if it is) or 0 (if it is not).
    prog = [3,9,8,9,10,9,4,9,99,-1,8]
    run_test(prog, stdin=[0], expected_out=[0])
    run_test(prog, stdin=[8], expected_out=[1])

    # Using position mode, consider whether the input is less than 8; output 1
    # (if it is) or 0 (if it is not).
    prog = [3,9,7,9,10,9,4,9,99,-1,8]
    run_test(prog, stdin=[7], expected_out=[1])
    run_test(prog, stdin=[9], expected_out=[0])

    # Using immediate mode, consider whether the input is equal to 8; output 1
    # (if it is) or 0 (if it is not).
    prog = [3,3,1108,-1,8,3,4,3,99]
    run_test(prog, stdin=[8], expected_out=[1])
    run_test(prog, stdin=[9], expected_out=[0])

    # Using immediate mode, consider whether the input is less than 8; output 1
    # (if it is) or 0 (if it is not).
    prog = [3,3,1107,-1,8,3,4,3,99]
    run_test(prog, stdin=[7], expected_out=[1])
    run_test(prog, stdin=[9], expected_out=[0])

    # Here are some jump tests that take an input, then output 0 if the input
    # was zero or 1 if the input was non-zero:
    prog = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]  # using position mode
    run_test(prog, stdin=[0], expected_out=[0])
    run_test(prog, stdin=[4], expected_out=[1])

    prog = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]  # using immediate mode
    run_test(prog, stdin=[0], expected_out=[0])
    run_test(prog, stdin=[4], expected_out=[1])


def test_day5_larger():
    """
    The above example program uses an input instruction to ask for a single
    number. The program will then output 999 if the input value is below 8,
    output 1000 if the input value is equal to 8, or output 1001 if the input
    value is greater than 8.
    """
    prog = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
            1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
            999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
    run_test(prog, stdin=[7], expected_out=[999])
    run_test(prog, stdin=[8], expected_out=[1000])
    run_test(prog, stdin=[9], expected_out=[1001])


def test_day9_base():
    program = [109, 19, 109, 6, 99]
    interpreter = Interpreter(program)
    interpreter.base = 2000
    interpreter.interpret(break_on_output=False)
    assert interpreter.base == 2025


def test_day9_relative():
    program = [109,6,21001,9,25,1,104,0,99,49]
    ret = interpret_intcode(program)
    assert ret.stdout == [74]


def test_day9_quine():
    quine = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
    run_test(quine, expected_out=quine)


def test_day9_relative():
    run_test([109, -1, 4, 1, 99], expected_out=[-1])
    run_test([109, -1, 104, 1, 99], expected_out=[1])
    run_test([109, -1, 204, 1, 99], expected_out=[109])
    run_test([109, 1, 9, 2, 204, -6, 99], expected_out=[204])
    run_test([109, 1, 109, 9, 204, -6, 99], expected_out=[204])
    run_test([109, 1, 209, -1, 204, -106, 99], expected_out=[204])
    run_test([109, 1, 3, 3, 204, 2, 99], stdin=[69], expected_out=[69])
    run_test([109, 1, 203, 2, 204, 2, 99], stdin=[1337], expected_out=[1337])


def test_fac():
    # factorial test
    fac = [3,29,1007,29,2,28,1005,28,24,2,27,29,27,1001,29,-1,29,1101,0,0,28,1006,28,2,4,27,99,1,0,0]
    res = interpret_intcode(fac, [4]) 
    assert res.stdout == [24]
