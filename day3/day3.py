import re
import timeit

with open("day3/in3.txt") as in3:
    data = in3.readlines()


def is_valid_part(potential_part, data):
    include_top = potential_part[1] > 0
    include_bottom = potential_part[1] < len(data) - 1
    include_left = potential_part[2] > 0
    include_right = potential_part[3] < len(data[0]) - 1

    adjacent = ""
    if include_top:
        adjacent += data[potential_part[1] - 1][
            potential_part[2] - 1
            if include_left
            else potential_part[2] : potential_part[3] + 2
            if include_right
            else potential_part[3] + 1
        ]

    if include_bottom:
        adjacent += data[potential_part[1] + 1][
            potential_part[2] - 1
            if include_left
            else potential_part[2] : potential_part[3] + 2
            if include_right
            else potential_part[3] + 1
        ]

    if include_left:
        adjacent += data[potential_part[1]][potential_part[2] - 1]

    if include_right:
        adjacent += data[potential_part[1]][potential_part[3] + 1]

    return any([c not in "0123456789.\n" for c in adjacent])


def part1(data):
    potential_parts = []
    for idx, line in enumerate(data):
        for m in re.finditer("\d+", line):
            # (part_number, y, x1, x2)
            potential_parts.append((int(m.group(0)), idx, m.start(0), m.end(0) - 1))

    out = 0
    for potential_part in potential_parts:
        if is_valid_part(potential_part, data):
            out += potential_part[0]

    return out


def part2(data):
    potential_parts = []
    for idx, line in enumerate(data):
        for m in re.finditer("\d+", line):
            # (part_number, y, x1, x2)
            potential_parts.append((int(m.group(0)), idx, m.start(0), m.end(0) - 1))

    parts = []
    for potential_part in potential_parts:
        if is_valid_part(potential_part, data):
            parts.append(potential_part)

    out = 0
    for idx, line in enumerate(data):
        for potential_gear in re.finditer(r"\*", line):
            pos = potential_gear.start()
            potential_parts = [
                part
                for part in parts
                if part[1] == idx - 1 or part[1] == idx or part[1] == idx + 1
            ]

            adjacent_parts = [
                potential_part
                for potential_part in potential_parts
                if any(
                    [
                        idx >= pos - 1 and idx <= pos + 1
                        for idx in list(range(potential_part[2], potential_part[3] + 1))
                    ]
                )
            ]

            if len(adjacent_parts) == 2:
                out += adjacent_parts[0][0] * adjacent_parts[1][0]

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
    f"Part 2 answer: {part2_answer}. Ran in {sum(ends) / len(ends) - sum(starts) / len(starts)} seconds on average."
)
