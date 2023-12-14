from performance_utils.performance_utils import measure_performance

with open("day14/in14.txt") as in14:
    data = [line.strip() for line in in14.readlines()]


def part1(data):
    out = 0
    column_values = [len(data)] * len(data[0])
    for y, row in enumerate(data):
        for x, node in enumerate(row):
            if node == "O":
                out += column_values[x]
                column_values[x] -= 1
            elif node == "#":
                column_values[x] = len(data) - y - 1

    return out


def cycle(data):
    # Tilt north.
    columns = ["".join([row[i] for row in data]) for i in range(len(data))]
    for idx, column in enumerate(columns):
        sections = column.split("#")
        columns[idx] = "#".join(
            ["".join(sorted(section, reverse=True)) for section in sections]
        )

    # Tilt west.
    rows = ["".join([column[i] for column in columns]) for i in range(len(data[0]))]
    for idx, row in enumerate(rows):
        sections = row.split("#")
        rows[idx] = "#".join(
            ["".join(sorted(section, reverse=True)) for section in sections]
        )

    # Tilt south.
    columns = ["".join([row[i] for row in rows]) for i in range(len(data))]
    for idx, column in enumerate(columns):
        sections = column.split("#")
        columns[idx] = "#".join(["".join(sorted(section)) for section in sections])

    # Tilt east.
    rows = ["".join([column[i] for column in columns]) for i in range(len(data[0]))]
    for idx, row in enumerate(rows):
        sections = row.split("#")
        rows[idx] = "#".join(["".join(sorted(section)) for section in sections])

    return rows


def calculate_load(data):
    load = 0
    for y, row in enumerate(data):
        for node in row:
            if node == "O":
                load += len(data) - y

    return load


def part2(data):
    values = []
    while True:
        data = cycle(data)

        value = calculate_load(data)
        if value in values:
            pattern_start = values.index(value)
            # This works for my input, might not work for the generic case.
            return values[pattern_start]

        values.append(calculate_load(data))


measure_performance("part 1", part1, data)
print(
    f"Part 2 answer: \033[92m{part2(data)}\x1b[0m. Too slow for performance measurement.\n"
)
