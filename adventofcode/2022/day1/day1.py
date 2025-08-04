def main(content):
   inventories = [x.rstrip().split("\n") for x in content.split("\n\n")]
   calories = sorted((sum(int(y) for y in x) for x in inventories), reverse=True)
   print("Part 1: ", calories[0])
   print("Part 2: ", sum(calories[:3]))


if __name__ == "__main__":
    import sys
    infile = sys.argv[1]
    with open(infile) as f:
        content = f.read()
        main(content)

