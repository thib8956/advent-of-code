
total = 0
numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0]

with open("input.txt") as f:
    data = [int(x) for x in f.readline().split(',')]

for i in data:
    if i == 0:
        numbers[0] += 1
    if i == 1:
        numbers[1] += 1
    if i == 2:
        numbers[2] += 1
    if i == 3:
        numbers[3] += 1
    if i == 4:
        numbers[4] += 1
    if i == 5:
        numbers[5] += 1
    if i == 6:
        numbers[6] += 1
    if i == 7:
        numbers[7] += 1
    if i == 8:
        numbers[8] += 1

def rotate(l):
    return l[1:] + l[:1]

for j in range(256):
    numbers = rotate(numbers)
    numbers[6] += numbers[8]
    print(f'DAY {j+1} AMOUNT OF FISH: {sum(numbers)}')
