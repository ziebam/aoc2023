import re

with open("day1/in1.txt") as in1:
    data = in1.readlines()


def part1(data):
    out = 0
    for line in data:
        str_digits = []
        for c in line.strip():
            if c in "123456789":
                str_digits.append(c)

        out += int(f"{str_digits[0]}{str_digits[-1]}")

    return out


def part2(data):
    str_to_digit_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    out = 0
    for line in data:
        matching_keys = []
        for key in str_to_digit_map.keys():
            if key in line:
                matching_keys.append(key)

        match_indices = {}
        for matching_key in matching_keys:
            if matching_key in line:
                for match in [m.start() for m in re.finditer(matching_key, line)]:
                    match_indices[match] = matching_key

        for idx, key in enumerate(sorted(match_indices.keys(), reverse=True)):
            if idx == 0 or idx == len(match_indices.keys()) - 1:
                line = (
                    line[:key] + str_to_digit_map[match_indices[key]] + line[key + 1 :]
                )

        str_digits = []
        for c in line.strip():
            if c in "123456789":
                str_digits.append(c)

        out += int(f"{str_digits[0]}{str_digits[-1]}")

    return out


print(part2(data))
