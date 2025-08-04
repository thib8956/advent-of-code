def parse_tickets(lines):
    tickets = []
    for line in lines:
        _, nums = line.rstrip().split(": ")
        winning, played = nums.split(" | ")
        winning, played = set(winning.split()), set(played.split())
        tickets.append((winning, played))
    return tickets


def part1(tickets):
    total = 0
    for ticket in tickets:
        winning, played = ticket
        num_wins = len(winning.intersection(played))
        points = 0 if num_wins == 0 else 2**(num_wins-1)
        total += points
    print(f"part 1, total={total}")


def part2(tickets):
    tickets = [[1, t] for t in tickets]
    for index, ticket in enumerate(tickets):
        mult = ticket[0]
        winning, played = ticket[1]
        num_wins = len(winning.intersection(played))
        for i in range(index+1, index+1+num_wins):
            tickets[i][0] += mult
    num_tickets = sum(n for n, _ in tickets)
    print(f"part 2, number of tickets: {num_tickets}")


def main(f):
    tickets = parse_tickets(f)
    part1(tickets)
    part2(tickets)


if __name__ == "__main__":
    import sys
    infile = sys.argv[1]
    with open(infile) as f:
        main(f)

