import itertools

with open("day12/in12.txt") as in12:
    data = [line.strip() for line in in12.readlines()]


def get_combinations(length):
    yield from itertools.product(*([".#"] * length))


def part1(data):
    out = 0
    for idx, line in enumerate(data):
        springs, records = line.split()
        records = [int(r) for r in records.split(",")]

        unknowns = 0
        for c in springs:
            if c == "?":
                unknowns += 1

        combinations = get_combinations(unknowns)
        for combination in combinations:
            new_springs = springs[:]
            for idx in range(len(combination)):
                new_springs = new_springs.replace("?", combination[idx], 1)

            operational_counts = []
            current_count = 0
            for spring in new_springs:
                if spring == ".":
                    if current_count > 0:
                        operational_counts.append(current_count)
                    current_count = 0
                else:
                    current_count += 1

            if current_count > 0:
                operational_counts.append(current_count)

            if operational_counts == records:
                out += 1

    return out


print(
    f"Part 1 answer: \033[92m{part1(data)}\x1b[0m. Too slow for performance measurement.\n"
)
