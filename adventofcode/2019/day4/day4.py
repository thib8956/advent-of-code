#! /usr/bin/env python3


def check_increase(number):
    num = str(number)
    for i in range(len(num) - 1):
        if num[i+1] < num[i]:
            return False
    return True

def check_adjacent(number):
    num = str(number)
    for digit in num:
        count = num.count(digit)
        if count == 2: # Part one : <= 2
            return True
    return False


def tests():
    assert check_increase(123456) == True
    assert check_increase(123454) == False
    assert check_adjacent(112345) == True
    assert check_adjacent(123445) == True
    assert check_adjacent(123456) == False


def main(start, end):
    matches = 0
    for n in range(start, end + 1):
        if check_increase(n) and check_adjacent(n):
            matches += 1
    return matches

if __name__ == "__main__":
    tests()
    print("Matches : ", main(367479, 893698))
