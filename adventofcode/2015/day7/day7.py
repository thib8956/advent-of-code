#!/usr/bin/env python3
import fileinput


def parse_circuit(inp):
    instructions = {}
    # dst: (OP, ARGS)
    for line in inp:
        op, dst = line.split(" -> ")
        op = op.split(" ")
        if len(op) == 1:  # ASSIGN
            src = op[0]
            instructions[dst] = ("ASSIGN", src)
        elif len(op) == 2:  # NOT
            assert op[0] == "NOT"
            instructions[dst] = ("NOT", op[1])
        elif len(op) == 3:  # BINARY OP
            instructions[dst] = (op[1], (op[0], op[2]))
    return instructions


def main(inp):
    instructions = parse_circuit(inp)
    res = evaluate_instruction("a", instructions)
    print("Part 1: ", res)
    instructions["b"] = ("ASSIGN", str(res))
    res = evaluate_instruction("a", instructions, state={})  # reset state
    print("Part 2: ", res)


def evaluate_instruction(start_wire, instructions, state={}):
    if start_wire in state:
        return state[start_wire]

    op, args = instructions[start_wire]
    result = -1
    if op == "ASSIGN":
        if args.isdigit():
            result = int(args)
        else:
            result = evaluate_instruction(args, instructions, state)
    elif op == "NOT":
        if args.isdigit():
            result = 65535 - int(args)
        else:
            result = 65535 - evaluate_instruction(args, instructions, state)
    elif op in ["AND", "OR", "LSHIFT", "RSHIFT"]:
        left, right = args
        if left.isdigit():
            left = int(left)
        else:
            left = evaluate_instruction(left, instructions, state)
        if right.isdigit():
            right = int(right)
        else:
            right = evaluate_instruction(right, instructions, state)
        match op:
            case "OR":
                result = left | right
            case "AND":
                result = left & right
            case "LSHIFT":
                result = left << right
            case "RSHIFT":
                result = left >> right
            case _:
                assert False, "Unreachable"
    else:
        assert False, "Unreachable"

    state[start_wire] = result
    return result


if __name__ == "__main__":
    lines = [x.rstrip() for x in fileinput.input()]
    main(lines)
