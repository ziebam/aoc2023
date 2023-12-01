import re
import timeit

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


starts = []
ends = []
for i in range(1000):
    starts.append(timeit.default_timer())
    part1_answer = part1(data)
    ends.append(timeit.default_timer())

print(
    f"Part 1 answer: {part1_answer}. Ran in {sum(ends) / len(ends) - sum(starts) / len(starts)} seconds on average."
)

starts = []
ends = []
for i in range(1000):
    starts.append(timeit.default_timer())
    part2_answer = part2(data)
    ends.append(timeit.default_timer())
print(
    f"Part 2 answer: {part2(data)}. Ran in {sum(ends) / len(ends) - sum(starts) / len(starts)} seconds on average."
)
