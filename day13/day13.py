from performance_utils.performance_utils import measure_performance

with open("day13/in13.txt") as in13:
    data = [
        [row.strip() for row in pattern.split()]
        for pattern in in13.read().split("\n\n")
    ]


def find_reflection(pattern, orig_reflection=None):
    columns = [[] for _ in range(len(pattern[0]))]
    for y, row in enumerate(pattern):
        for x, element in enumerate(row):
            columns[x].append(element)

        if y == 0:
            continue

        if row == pattern[y - 1]:
            if all(
                pattern[y1] == pattern[y2]
                for y1, y2 in zip(range(y + 1, len(pattern)), range(y - 2, -1, -1))
            ) and (not orig_reflection or ("row", y) != orig_reflection):
                return ("row", y)
    else:
        for x, column in enumerate(columns):
            if x == 0:
                continue
            if column == columns[x - 1]:
                if all(
                    columns[x1] == columns[x2]
                    for x1, x2 in zip(range(x + 1, len(columns)), range(x - 2, -1, -1))
                ) and (not orig_reflection or ("col", x) != orig_reflection):
                    return ("col", x)


def part1(data):
    out = 0
    for pattern in data:
        reflection = find_reflection(pattern)
        if reflection[0] == "row":
            out += reflection[1] * 100
        else:
            out += reflection[1]

    return out


def part2(data):
    out = 0

    for pattern in data:
        orig_reflection = find_reflection(pattern)
        new_reflection = None
        for i in range(len(pattern)):
            for j in range(len(pattern[0])):
                new_pattern = pattern[:]
                new_pattern[i] = (
                    new_pattern[i][:j]
                    + ("." if new_pattern[i][j] == "#" else ".")
                    + new_pattern[i][j + 1 :]
                )

                new_reflection = find_reflection(new_pattern, orig_reflection)

                if new_reflection:
                    break

            if new_reflection:
                break

        if new_reflection[0] == "row":
            out += new_reflection[1] * 100
        else:
            out += new_reflection[1]

    return out


measure_performance("part 1", part1, data)
measure_performance("part 2", part2, data, warmup_runs=100, actual_runs=1000)
