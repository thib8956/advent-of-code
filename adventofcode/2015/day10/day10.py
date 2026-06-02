#!/usr/bin/env python3
import fileinput


def look_and_say(seq):
    """
    Describe each element by counting the number of consecutive digits
    of the same value and appending that count followed by the digit itself.
    """
    ret = []
    current_char = seq[0]
    current_count = 1
    for c in seq[1:]:
        if c == current_char:
            current_count += 1
        else:
            ret.append(str(current_count))
            ret.append(current_char)
            current_char = c
            current_count = 1

    # last char
    ret.append(str(current_count))
    ret.append(current_char)
    return "".join(ret)


def main(inp):
    inp = list(inp)
    for _ in range(40):
        inp = look_and_say(inp)
    print("Part 1:", len(inp))

    for _ in range(10):  # 40 + 10 = 50
        inp = look_and_say(inp)
    print("Part 2:", len(inp))


if __name__ == "__main__":
    lines = next(x.rstrip() for x in fileinput.input())
    main(lines)
