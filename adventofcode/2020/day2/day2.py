import part1
import part2


def main(lines):
    part1.main(lines)
    part2.main(lines)


if __name__ == "__main__":
    import fileinput
    lines = [x for x in fileinput.input()]
    main(lines)

