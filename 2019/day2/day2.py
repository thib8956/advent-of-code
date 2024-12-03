def interpret_intcode(input_prog):
    # Instruction pointer: index of the next element to be executed
    ip = 0
    while ip < len(input_prog):
        instruction = input_prog[ip]
        if instruction == 99:
            break

        elif instruction == 1:
            # The operands to sum are at the memory location ip+1 and ip+2.
            operands = (input_prog[input_prog[ip + 1]], input_prog[input_prog[ip + 2]])
            result = sum(operands)
            target = input_prog[ip + 3]
            input_prog[target] = result
            ip += 4

        elif instruction == 2:
            # The operands to multiply are at the memory location ip+1 and ip+2.
            operands = (input_prog[input_prog[ip + 1]], input_prog[input_prog[ip + 2]])
            result = operands[0] * operands[1]
            target = input_prog[ip + 3]
            input_prog[target] = result
            ip += 4


def tests():
    inputs = (
        [1, 0, 0, 0, 99],  # ADD 1 + 1 to location 0
        [2, 3, 0, 3, 99],  # MUL 2 * 3 to location 3
        [2, 4, 4, 5, 99, 0],
        [1, 1, 1, 4, 99, 5, 6, 0, 99],
    )
    expected_outputs = (
        [2, 0, 0, 0, 99],  # 1 + 1 = 2
        [2, 3, 0, 6, 99],  # 3 * 2 = 6
        [2, 4, 4, 5, 99, 9801],  # 99 * 99 = 9801
        [30, 1, 1, 4, 2, 5, 6, 0, 99],
    )
    for i, inp in enumerate(inputs):
        result = inp[:]
        interpret_intcode(result)
        assert (
            result == expected_outputs[i]
        ), f"Expected output for {inp} is {expected_outputs[i]}, but found {result} instead."
    print("All tests passed.")


def run_program(memory, noun, verb):
    memory[1] = noun
    memory[2] = verb
    interpret_intcode(memory)
    return memory[0]


if __name__ == "__main__":
    tests()
    with open("input.txt") as inp:
        memory = [int(x) for x in inp.readline().strip().split(",")]
        # Pass a copy to avoid modifying the original memory
        print("Part 1 answer: ", run_program(memory[:], 12, 2))

        # Part 2
        result = 0
        for verb in range(99):
            for noun in range(99):
                if run_program(memory[:], noun, verb) == 19690720:
                    print(f"Part 2: noun={noun}, verb={verb}")
                    print("Result = ", 100 * noun + verb)
                    break
