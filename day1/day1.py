import re

from performance_utils.performance_utils import measure_performance

with open("day1/in1.txt") as in1:
    data = in1.readlines()


def part1(data):
    out = 0
    for line in data:
        matches = re.findall("\d", line)
        out += int(matches[0]) * 10
        out += int(matches[-1])

    return out


def part2(data):
    regex = "(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
    str_to_digit = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    out = 0
    for line in data:
        matches = re.findall(regex, line)
        out += int(str_to_digit.get(matches[0], matches[0])) * 10
        out += int(str_to_digit.get(matches[-1], matches[-1]))

    return out


measure_performance("part 1", part1, data)
measure_performance("part 2", part2, data)
