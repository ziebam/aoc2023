# Hugely inspired by the amazing writeup at:
# https://www.reddit.com/r/adventofcode/comments/18hbbxe/2023_day_12python_stepbystep_tutorial_with_bonus/

import functools

from performance_utils.performance_utils import measure_performance

with open("day12/in12.txt") as in12:
    data = [line.strip() for line in in12.readlines()]


@functools.cache
def calculate_possibilities(record, groups):
    if not groups:
        if "#" not in record:
            return 1
        else:
            return 0

    if not record:
        return 0

    next_character = record[0]
    next_group = groups[0]

    def pound():
        this_group = record[:next_group]
        this_group = this_group.replace("?", "#")

        if this_group != next_group * "#":
            return 0

        if len(record) == next_group:
            if len(groups) == 1:
                return 1
            else:
                return 0

        if record[next_group] in "?.":
            return calculate_possibilities(record[next_group + 1 :], groups[1:])

        return 0

    def dot():
        return calculate_possibilities(record[1:], groups)

    if next_character == "#":
        possibilities = pound()

    elif next_character == ".":
        possibilities = dot()

    elif next_character == "?":
        possibilities = dot() + pound()

    else:
        raise RuntimeError("Unexpected character!")

    return possibilities


def part1(data):
    out = 0
    for line in data:
        record, raw_groups = line.split()
        groups = [int(i) for i in raw_groups.split(",")]

        out += calculate_possibilities(record, tuple(groups))

    return out


def part2(data):
    out = 0
    for line in data:
        raw_record, raw_groups = line.split()
        record = "?".join(raw_record for _ in range(5))
        raw_groups = ",".join(raw_groups for _ in range(5))
        groups = [int(group) for group in raw_groups.split(",")]

        out += calculate_possibilities(record, tuple(groups))

    return out


measure_performance("part 1", part1, data)
measure_performance("part 2", part2, data)
