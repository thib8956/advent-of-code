def main(content):
    table = str.maketrans("XYZ", "ABC")
    score = 0
    for c in content:
        c = c.translate(table)
        w = ord(c[-1]) - ord("A") + 1
        match c:
            case "A A" | "B B" | "C C": score += 3 + w
            case "A B" | "B C" | "C A": score += 6 + w
            case "A C" | "B A" | "C B": score += w
            case _: assert False, c
    print("Part 1: ", score)

    # x = lose, y = draw, z = win
    score = 0
    for c in content:
        outcome = c[-1]
        if outcome == "Y":
            w = ord(c[0]) - ord("A") + 1
            score += 3 + w
        elif outcome == "Z":
            index = ord(c[0]) - ord("A")
            play = "ABC"[(index + 1) % 3]
            w = ord(play) - ord("A") + 1
            score += 6 + w
        elif outcome == "X":
            index = ord(c[0]) - ord("A")
            w = ord("ABC"[index - 1]) - ord("A") + 1
            score += w
        else:
            assert False, outcome
    print(score)



if __name__ == "__main__":
    import fileinput
    #main(['A Y', 'B X', 'C Z'])
    main(list(l.rstrip() for l in fileinput.input()))

