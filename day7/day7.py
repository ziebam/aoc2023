# TODO: Convert types/ranks into an enum.

from collections import Counter

from performance_utils.performance_utils import measure_performance

with open("day7/in7.txt") as in7:
    data = [line.strip() for line in in7.readlines()]


STRENGTH_MAP_PART1 = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
STRENGTH_MAP_PART2 = {"T": 10, "J": 1, "Q": 12, "K": 13, "A": 14}


def get_type_part1(hand):
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


def get_type_part2(hand):
    if "J" not in hand:
        return get_type_part1(hand)

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
        strength = 0
        for idx, card in enumerate(hand):
            # Need to multiply by 2 since some cards values' are larger than 10,
            # which causes an overflow to the next highest digit (e.g. from tens to
            # hundreds), skewing the result.
            multiplier = 10 ** ((idx - 5) * (-1) * 2)
            if card in STRENGTH_MAP_PART1:
                strength += STRENGTH_MAP_PART1[card] * multiplier
            else:
                strength += int(card) * multiplier
        hands.append((hand, int(bid), strength, get_type_part1(hand)))

    for idx, hand in enumerate(sorted(hands, key=lambda x: (x[3], x[2]))):
        out += hand[1] * (idx + 1)

    return out


def part2(data):
    hands = []

    out = 0
    for line in data:
        hand, bid = line.split()
        strength = 0
        for idx, card in enumerate(hand):
            # Need to multiply by 2 since some cards values' are larger than 10,
            # which causes an overflow to the next highest digit (e.g. from tens to
            # hundreds), skewing the result.
            multiplier = 10 ** ((idx - 5) * (-1) * 2)
            if card in STRENGTH_MAP_PART2:
                strength += STRENGTH_MAP_PART2[card] * multiplier
            else:
                strength += int(card) * multiplier
        hands.append((hand, int(bid), strength, get_type_part2(hand)))

    for idx, hand in enumerate(sorted(hands, key=lambda x: (x[3], x[2]))):
        out += hand[1] * (idx + 1)

    return out


measure_performance("part 1", part1, data)
measure_performance("part 2", part2, data)
