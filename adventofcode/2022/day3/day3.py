from itertools import zip_longest
from functools import reduce
from operator import and_


def grouper(n, iterable):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args)


def split(x):
    return set(x[:len(x)//2]), set(x[len(x)//2:])


def get_priority(x):
    x = x.pop()
    prio = ord(x)
    if "a" <= x <= "z":
        prio -= ord("a") - 1
    else:
        prio -= ord("A") - 27
    return prio


def main(content):
    total = sum(get_priority(reduce(and_, split(l))) for l in content)
    print("Part 1: ", total)
    total =  sum(get_priority(reduce(and_, map(set, x))) for x in grouper(3, content))
    print("Part 2: ", total)


if __name__ == "__main__":
    import fileinput
    main(list(l.rstrip() for l in fileinput.input()))

