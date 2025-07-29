#! /usr/bin/env python3


def part1(instructions):
    instruction_pointer = 0
    accumulator = 0
    visited_instructions = set()
    while instruction_pointer not in visited_instructions:  # return before executing any instruction a second time
        if instruction_pointer >= len(instructions):  # stop the program when ip is out of bounds
            break
        visited_instructions.add(instruction_pointer)
        instruction, argument = instructions[instruction_pointer].split(" ")
        if instruction == "acc":
            accumulator += int(argument)
            instruction_pointer += 1
        elif instruction == "jmp":
            value = int(argument)
            instruction_pointer += value
        else:
            instruction_pointer += 1
    return instruction_pointer, accumulator


def part2(instructions):
    for index, line in enumerate(instructions):
        permutation = generate_permutation(instructions, line, index)
        if permutation is None:
            continue
        instruction_pointer, accumulator = part1(permutation)
        if instruction_pointer == len(permutation):
            return accumulator


def generate_permutation(instructions, line, index):
    permutation = instructions[:]
    instruction, arg = line.split(" ")
    if instruction == "acc":  # don't replace acc operations
        return
    elif instruction == "nop":
        permutation[index] = f"jmp {arg}"
    elif instruction == "jmp":
        permutation[index] = f"nop {arg}"
    return permutation


def main(inp):
    instructions = [line.rstrip() for line in fileinput.input()]
    print("Part 1 : (ip, acc) ", part1(instructions)[1])
    print("Part 2 : (ip, acc) ", part2(instructions))


if __name__ == "__main__":
    import fileinput
    main(fileinput.input())

