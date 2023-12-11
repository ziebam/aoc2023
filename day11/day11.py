from performance_utils.performance_utils import measure_performance

with open("day11/in11.txt") as in11:
    data = [line.strip() for line in in11.readlines()]


def solve(data, is_part_two):
    multiplier = 999_999 if is_part_two else 1

    galaxies = []
    empty_rows = []
    galaxy_counts_in_cols = [0] * len(data[0])
    for y, row in enumerate(data):
        row_has_galaxy = False
        for x, col in enumerate(row):
            if col == "#":
                row_has_galaxy = True
                galaxies.append((x, y))
                galaxy_counts_in_cols[x] += 1
        if not row_has_galaxy:
            empty_rows.append(y)

    empty_cols = [
        idx
        for idx, galaxy_count in enumerate(galaxy_counts_in_cols)
        if galaxy_count == 0
    ]

    out = 0
    for idx, galaxy in enumerate(galaxies):
        x1 = galaxy[0]
        y1 = galaxy[1]
        for paired_galaxy in galaxies[idx + 1 :]:
            x2 = paired_galaxy[0]
            y2 = paired_galaxy[1]

            extra_rows = len(
                [i for i in range(min(y1, y2), max(y1, y2)) if i in empty_rows]
            )
            extra_cols = len(
                [i for i in range(min(x1, x2), max(x1, x2)) if i in empty_cols]
            )

            out += abs(x2 - x1) + abs(y2 - y1) + (extra_rows + extra_cols) * multiplier

    return out


measure_performance("part 1", solve, data, False, warmup_runs=10, actual_runs=100)
measure_performance("part 2", solve, data, True, warmup_runs=10, actual_runs=100)
