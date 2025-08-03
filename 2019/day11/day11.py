# TODO replace PYTHONPATH hack with a proper solution, like making intcode an
# installed module https://stackoverflow.com/a/50194143
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).absolute().parent.parent / "intcode"))
from intcode import interpret_intcode, Interpreter


def paint(program, initial_state):
    interpreter = Interpreter(program)
    pos = 0 + 0j
    direction = 0 - 1j  # initially facing up ^
    colors = {}
    colors[pos] = initial_state
    while True:
        interpreter.stdin.append(colors.get(pos, 0))
        interpreter.interpret(break_on_output=True)
        interpreter.interpret(break_on_output=True)
        if interpreter.halted:
            return colors

        color = interpreter.stdout.pop(0)
        colors[pos] = color

        turn = interpreter.stdout.pop(0)
        if turn == 0:
            direction *= -1j  # turn left
        elif turn == 1:
            direction *= 1j  # turn right
        else:
            assert False

        pos += direction


def main(data, part=1):
    program = list(map(int, data.readline().rstrip().split(",")))
    if part == 1:
        colors = paint(program, initial_state=0)
        print("Part 1: ", len(colors))
    else:
        colors = paint(program, initial_state=1)
        part2(colors)


def part2(colors):
    min_x = int(min(x.real for x in colors.keys()))
    max_x = int(max(x.real for x in colors.keys()))
    min_y = int(min(x.imag for x in colors.keys()))
    max_y = int(max(x.imag for x in colors.keys()))
    for y in range(min_y, max_y + 1):
        l = []
        for x in range(min_x, max_x + 1):
            point = complex(x, y)
            l.append("\u2588" if point in colors and colors[point] == 1 else " ")
        print("".join(l))


if __name__ == "__main__":
    import fileinput
    with fileinput.input() as f:
        main(f, part=1)
    with fileinput.input() as f:
        #main(f, part=2)  # FIXME unable to run both parts simultaneously

