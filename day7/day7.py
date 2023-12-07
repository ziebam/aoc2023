# TODO: Convert types/ranks into an enum.

from collections import Counter

from performance_utils.performance_utils import measure_performance

with open("day7/in7.txt") as in7:
    data = [line.strip() for line in in7.readlines()]


STRENGTH_MAP_PART1 = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
STRENGTH_MAP_PART2 = {"T": 10, "J": 1, "Q": 12, "K": 13, "A": 14}


def get_rank_part1(hand):
    c = Counter(hand)
    counts = c.values()

    if 5 in counts:
        return 6

    if 4 in counts:
        return 5

    if 3 in counts and 2 in counts:
        return 4

    if 3 in counts:
        return 3

    if 2 in counts:
        if len(counts) == 3:
            return 2
        else:
            return 1

    return 0


def get_rank_part2(hand):
    if "J" not in hand:
        return get_rank_part1(hand)

    c = Counter(hand)
    counts = c.values()

    if c["J"] == 5 or c["J"] == 4:
        return 6
    if c["J"] == 3:
        if 2 in counts:
            return 6
        else:
            return 5
    if c["J"] == 2:
        if 3 in counts:
            return 6
        if len(counts) == 3:
            return 5
        else:
            return 3
    if c["J"] == 1:
        if 4 in counts:
            return 6
        if 3 in counts:
            return 5
        if len(counts) == 3:
            return 4
        if 2 in counts:
            return 3
        else:
            return 1

    return 0


def part1(data):
    hands = []

    out = 0
    for line in data:
        hand, bid = line.split()
        current_hand = [hand, int(bid), get_rank_part1(hand)]
        for idx, card in enumerate(hand):
            if card in STRENGTH_MAP_PART1:
                current_hand.append(STRENGTH_MAP_PART1[card])
            else:
                current_hand.append(int(card))
        hands.append(current_hand)

    for idx, hand in enumerate(
        sorted(hands, key=lambda x: (x[2], x[3], x[4], x[5], x[6], x[7]))
    ):
        out += hand[1] * (idx + 1)

    return out


def part2(data):
    hands = []

    out = 0
    for line in data:
        hand, bid = line.split()
        current_hand = [hand, int(bid), get_rank_part2(hand)]
        for idx, card in enumerate(hand):
            if card in STRENGTH_MAP_PART2:
                current_hand.append(STRENGTH_MAP_PART2[card])
            else:
                current_hand.append(int(card))
        hands.append(current_hand)

    for idx, hand in enumerate(
        sorted(hands, key=lambda x: (x[2], x[3], x[4], x[5], x[6], x[7]))
    ):
        out += hand[1] * (idx + 1)

    return out


measure_performance("part 1", part1, data)
measure_performance("part 2", part2, data)
