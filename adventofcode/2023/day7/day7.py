from collections import Counter


def calculate_rank(hand, part2=False):
    card_ranks = {'2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'J': 10, 'Q': 11, 'K': 12, 'A': 13}
    if part2:
        # in part2, jokers are the weakest card
        card_ranks['J'] = 0
    # substitute cards with their ranks to make them sortable
    hand = [card_ranks[c] for c in hand]
    cnt = Counter(hand)
    
    if part2 and cnt[0] != 5:  # edge case if hand == 'JJJJJ'
        # substitute jokers with the most common card that isn't a joker
        most_common_card = cnt.most_common(2)[0][0] if cnt.most_common(2)[0][0] != 0 else cnt.most_common(2)[1][0]
        new_hand = [most_common_card if c == 0 else c for c in hand]
        cnt = Counter(new_hand)
    
    rank = 0
    match sorted(cnt.values()):
        case [5]: rank = 7
        case [1, 4]: rank = 6
        case [2, 3]: rank = 5
        case [1, 1, 3]: rank = 4
        case [1, 2, 2]: rank = 3
        case [1, 1, 1, 2]: rank = 2
        case [1, 1, 1, 1, 1]: rank = 1
    # return rank, and hand as a tiebreaker
    return (rank, hand)

def parse_input(inp):
    hands = [l.strip().split() for l in inp.strip().split("\n")]
    return hands


def calculate_wins(hands, part2=False):
    total = 0
    hands = sorted(hands, key=lambda hb: calculate_rank(hb[0], part2=part2))
    for rank, hand in enumerate(hands):
        hand, bid = hand
        total += (rank + 1) * int(bid)
    return total


if __name__ == "__main__":
    sample_input = """
        32T3K 765
        T55J5 684
        KK677 28
        KTJJT 220
        QQQJA 483
    """
    res = calculate_wins(parse_input(sample_input))
    print(f"part 1 example: {res}")
    assert res == 6440

    res = calculate_wins(parse_input(sample_input), part2=True)
    print(f"part 2 example: {res}")
    assert res == 5905
    
    import sys
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            inp = parse_input(f.read())
            
            res = calculate_wins(inp)
            print(f"Part 1, res={res}")
            
            res = calculate_wins(inp, part2=True)
            print(f"Part 2, res={res}")
