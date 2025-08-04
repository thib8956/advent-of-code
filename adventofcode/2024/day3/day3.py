import re


def main(content):
    operations = re.findall(r"(?:mul\((\d+),(\d+)\))|(do\(\))|(don't\(\))", content)

    # filter only mul instructions for part1, format: ('498', '303', '', '')
    mul_operations = [x for x in operations if x[0].isnumeric()]
    total = sum(int(a) * int(b) for a, b, *_rest in mul_operations)
    print("Part 1: ", total)

    do_mul = True
    total = 0
    for op in operations:
        token = "".join(op)
        print(token)
        if token.startswith("don't"):
            do_mul = False
            print("disable_mul")
        elif token.startswith("do"):
            do_mul = True
        elif token.isnumeric():
            if do_mul:
                a, b, *_rest = op
                total += int(a) * int(b)
        else:
            raise RuntimeError(f"Invalid token {token}")
    print("Part 2: ", total)


if __name__ == "__main__":

    import sys
    infile = sys.argv[1]
    
    with open(infile) as f:
        content = f.read()
        main(content)

