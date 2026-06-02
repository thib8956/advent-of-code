#!/usr/bin/env python3
import fileinput


def evaluate(s: str):
    s = s[1:-1]  # remove surrounding quotes
    out = []
    i = 0
    while i < len(s):
        if s[i] == "\\":
            nxt = s[i + 1]
            if nxt == '"':
                out.append('"')
                i += 2
            elif nxt == "\\":
                out.append("\\")
                i += 2
            elif nxt == "x":
                c = chr(int(s[i + 2 : i + 4], 16))
                out.append(c)
                i += 4
        else:
            out.append(s[i])
            i += 1
    return "".join(out)


def part1(inp):
    total = 0
    for line in inp:
        code_len = len(line)
        evaluated = evaluate(line)
        str_len = len(evaluated)
        total += code_len - str_len
    return total


def escape(s):
    return


def part2(inp):
    total = 0
    trans = str.maketrans({"\\": r"\\", '"': '\\"'})
    for line in inp:
        code_len = len(line)
        escaped = f'"{line.translate(trans)}"'
        escaped_len = len(escaped)
        total += escaped_len - code_len
    return total


def main(inp):
    print("Part 1: ", part1(inp))
    print("Part 2: ", part2(inp))


def tests():
    inp = [
        '""',
        '"abc"',
        '"aaa\\"aaa"',
        '"\\x27"',
        # r'"vvdnb\\x\\uhnxfw\"dpubfkxfmeuhnxisd"',
    ]
    part2(inp)


if __name__ == "__main__":
    lines = [x.rstrip() for x in fileinput.input()]
    main(lines)
