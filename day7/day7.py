from collections import Counter
from enum import Enum

from performance_utils.performance_utils import measure_performance

with open("day7/in7.txt") as in7:
    data = [line.strip() for line in in7.readlines()]


class Rank(Enum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    FULL_HOUSE = 4
    FOUR_OF_A_KIND = 5
    FIVE_OF_A_KIND = 6

    def __lt__(self, b):
        return self.value < b.value


def get_rank_without_jokers(hand):
    c = Counter(hand)
    counts = c.values()

    if 5 in counts:  # ex. AAAAA
        return Rank.FIVE_OF_A_KIND

    if 4 in counts:  # ex. AAAAK
        return Rank.FOUR_OF_A_KIND

    if 3 in counts and 2 in counts:  # ex. AAAKK
        return Rank.FULL_HOUSE

    if 3 in counts:  # ex. AAAKQ
        return Rank.THREE_OF_A_KIND

    if 2 in counts:
        if len(counts) == 3:  # ex. AAKKQ
            return Rank.TWO_PAIR
        else:  # ex. AAKQJ
            return Rank.ONE_PAIR

    return Rank.HIGH_CARD  # ex. AKQJT


def get_rank_with_jokers(hand):
    if "J" not in hand:
        return get_rank_without_jokers(hand)

    c = Counter(hand)
    counts = c.values()

    if c["J"] == 5 or c["J"] == 4:  # ex. JJJJJ or JJJJA
        return Rank.FIVE_OF_A_KIND
    if c["J"] == 3:
        if 2 in counts:  # ex. JJJAA
            return Rank.FIVE_OF_A_KIND
        else:  # ex. JJJAK
            return Rank.FOUR_OF_A_KIND
    if c["J"] == 2:
        if 3 in counts:  # ex. JJAAA
            return Rank.FIVE_OF_A_KIND
        if len(counts) == 3:  # ex. JJAAK
            return Rank.FOUR_OF_A_KIND
        else:  # ex. JJAKQ
            return Rank.THREE_OF_A_KIND
    if c["J"] == 1:
        if 4 in counts:  # ex. JAAAA
            return Rank.FIVE_OF_A_KIND
        if 3 in counts:  # ex. JAAAK
            return Rank.FOUR_OF_A_KIND
        if len(counts) == 3:  # ex. JAAKK
            return Rank.FULL_HOUSE
        if 2 in counts:  # ex. JAAKQ
            return Rank.THREE_OF_A_KIND
        else:  # ex. JAKQT
            return Rank.ONE_PAIR

    # The above cover all possible cases, so there's no need for a fallthrough `return`.


def get_hands(data, rank_getter, strength_map):
    hands = []
    for line in data:
        hand, bid = line.split()
        current_hand = [hand, int(bid), rank_getter(hand)]
        for card in hand:
            if card in strength_map:
                current_hand.append(strength_map[card])
            else:
                current_hand.append(int(card))
        hands.append(current_hand)

    return hands


def get_winnings(hands):
    out = 0
    for idx, hand in enumerate(
        # Sorted first by rank (e.g. "three of a kind"), and then by each card starting from the first one.
        sorted(hands, key=lambda x: (x[2], x[3], x[4], x[5], x[6], x[7]))
    ):
        out += hand[1] * (idx + 1)

    return out


def part1(data):
    STRENGTH_MAP = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    hands = get_hands(data, get_rank_without_jokers, STRENGTH_MAP)

    return get_winnings(hands)


def part2(data):
    STRENGTH_MAP = {"T": 10, "J": 1, "Q": 12, "K": 13, "A": 14}
    hands = get_hands(data, get_rank_with_jokers, STRENGTH_MAP)

    return get_winnings(hands)


measure_performance("part 1", part1, data)
measure_performance("part 2", part2, data)
