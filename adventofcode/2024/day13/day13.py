def parse_machine(machine):
    btn_a, btn_b, prize = [x.split(": ")[1].split(", ") for x in machine]
    btn_a = [int(x.split("+")[1]) for x in btn_a]
    btn_b = [int(x.split("+")[1]) for x in btn_b]
    prize = [int(x.split("=")[1]) for x in prize]
    return (btn_a, btn_b, prize)


def solve(btn_a, btn_b, prize, offset=0):
    a_x, a_y = btn_a
    b_x, b_y = btn_b
    p_x, p_y = [p + offset for p in prize]
    # apply Cramer's rule to solve the 2x2 system
    A = (p_x*b_y - p_y*b_x) / (a_x*b_y - a_y*b_x)
    B = (a_x*p_y - a_y*p_x) / (a_x*b_y - a_y*b_x)
    if A.is_integer() and B.is_integer():
        return int(A), int(B)
    return None, None


def main(content):
    part1 = 0
    part2 = 0
    for machine in content:
        btn_a, btn_b, prize = parse_machine(machine)

        A, B = solve(btn_a, btn_b, prize)
        if A is not None and B is not None:
            part1 += 3*A + B

        A, B = solve(btn_a, btn_b, prize, 10000000000000)
        if A is not None and B is not None:
            part2 += 3*A + B
        
    print("Part 1: ", part1)
    print("Part 2: ", part2)


if __name__ == "__main__":
    import sys
    infile = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
    with open(infile) as f:
        content = f.read().split("\n\n")
        content = [x.rstrip().split("\n") for x in content]
        main(content)

