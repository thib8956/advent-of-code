#!/usr/bin/env python3
from collections import defaultdict


def part1(infile):
    memory = defaultdict(int)
    for line in infile:
        left, right = line.split("=")
        if left.startswith("mask"):
            one_mask = right.translate(right.maketrans("X", "0"))
            zero_mask = right.translate(right.maketrans("X10", "001"))
        else:
            address = int(left.split("[")[1].rstrip("] "))  # mem[42] -> 42
            value = int(right.rstrip())
            memory[address] = value & ~int(zero_mask, 2) | int(one_mask, 2)

    return sum(memory.values())


def part2(infile):
    memory = defaultdict(int)
    for line in infile:
        left, right = line.split(" = ")
        if left.startswith("mask"):
            mask = right.rstrip()
        else:
            value = right.rstrip()
            address = apply_mask(left.split("[")[1].rstrip("] "), mask)
            for addr in generate_floating_addresses(address):
                memory[int(addr, 2)] = int(value)
    return sum(memory.values())


def apply_mask(address, mask):
    address = bin(int(address)).lstrip("0b")
    address = address.zfill(36)
    for index, bit in enumerate(mask):
        if bit == "1":
            address = address[:index] + "1" + address[index + 1 :]
        elif bit == "X":
            address = address[:index] + "X" + address[index + 1 :]
    return address


def generate_floating_addresses(address):
    index = address.find("X")
    if index == -1:
        return [address]
    a1 = generate_floating_addresses(address[:index] + "0" + address[index + 1 :])
    a2 = generate_floating_addresses(address[:index] + "1" + address[index + 1 :])
    return a1 + a2


if __name__ == "__main__":
    import fileinput
    lines = [x for x in fileinput.input()]
    print(part1(lines))
    print(part2(lines))
