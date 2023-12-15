from performance_utils.performance_utils import measure_performance

with open("day06/in06.txt") as in06:
    data = in06.readlines()


def part1(data):
    out = 1

    for time, record in zip(
        data[0].split(":")[1].split(), data[1].split(":")[1].split()
    ):
        time = int(time)
        record = int(record)

        delta = time * time - 4 * record
        sqrt_delta = delta**0.5
        x1 = int((time - sqrt_delta) / 2)
        x2 = int((time + sqrt_delta) / 2)

        out *= abs(x1 - x2)

    return out


def part2(data):
    time = int("".join(time_part for time_part in data[0].split(":")[1].split()))
    record = int(
        "".join(distance_part for distance_part in data[1].split(":")[1].split())
    )

    delta = time * time - 4 * record
    sqrt_delta = delta**0.5
    x1 = int((time - sqrt_delta) / 2)
    x2 = int((time + sqrt_delta) / 2)

    return abs(x1 - x2)


measure_performance("part 1", part1, data, unit="microseconds")
measure_performance("part 2", part2, data, unit="microseconds")
