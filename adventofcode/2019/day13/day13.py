#!/usr/bin/env python3
# TODO replace PYTHONPATH hack with a proper solution, like making intcode an
# installed module https://stackoverflow.com/a/50194143
import sys
import time
from itertools import zip_longest
from pathlib import Path
from collections import defaultdict, Counter
from dataclasses import dataclass

sys.path.append(str(Path(__file__).absolute().parent.parent / "intcode"))
from intcode import interpret_intcode, Interpreter

@dataclass
class State:
    grid: ...
    score = 0
    bounds = None
    paddle_pos = None
    ball_pos = None
    stopped = False


def grouper(n, iterable):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args)


def part1(program):
    interpreter = interpret_intcode(program)
    game = { (x, y): tile for x, y, tile in grouper(3, interpreter.stdout) }
    print("Part 1: ", len([x for x in game.values() if x == 2]))


def parse_map(output):
    grid = {}
    score = None
    for x, y, tile in grouper(3, output):
        if (x, y) == (-1, 0):
            score = tile
        else:
            grid[x,y] = tile
    paddle = next((k for k, v in grid.items() if v == 3), None)
    ball = next((k for k, v in grid.items() if v == 4), None)
    bounds = (max(x for x, y in grid.keys()),
              max(y for x, y in grid.keys()))
    return grid, bounds, score, paddle, ball


def update_state(state: State, stdout):
    grid, bounds, score, paddle, ball = parse_map(stdout)
    if ball is None:
        state.stopped = True
    if state.bounds is None:  # only set bounds the first time
        state.bounds = bounds
    if score is not None:
        state.score = score
    if paddle is not None:
        state.paddle_pos = paddle
    if ball is not None:
        state.ball_pos = ball
    if grid is None:
        state.grid = grid
    else:
        # merge grid
        for (x, y), v in grid.items():
            state.grid[x,y] = v
    return state


def part2(program):
    program[0] = 2
    interpreter = Interpreter(program)
    state = State({})
    while not interpreter.halted:
        interpreter.interpret(break_on_output=False, break_on_input=True)
        state = update_state(state, interpreter.stdout)
        if state.stopped:
            break
        #print_map(state)
        interpreter.stdout.clear()
        paddle_x, ball_x = state.paddle_pos[0], state.ball_pos[0]
        if paddle_x < ball_x:  # move right
            interpreter.stdin.append(1)
        elif paddle_x > ball_x:  # move left
            interpreter.stdin.append(-1)
        else:
            interpreter.stdin.append(0)
    print("Part 2: ", state.score)


def print_map(state):
    clear = "\033[2J"
    tiles = { 0: " ", 1: "#", 2: "~", 3: "_", 4: "O" }
    max_x, max_y = state.bounds
    print(clear)
    for y in range(max_y + 1):
        l = []
        for x in range(max_x + 1):
            tile = state.grid[x,y]
            l.append(tiles[tile])
        print("".join(l))
    time.sleep(1/60)


def main(inp):
    program = [int(x) for x in inp.readline().rstrip().split(",")]
    part1(program)
    part2(program)

if __name__ == "__main__":
    import sys
    infile = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
    with open(infile) as raw_input:
        main(raw_input)

