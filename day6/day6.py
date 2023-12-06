from performance_utils.performance_utils import measure_performance

with open("day6/in6.txt") as in6:
    data = in6.readlines()


def part1(data):
    out = 1

    for time, distance in zip(
        data[0].split(":")[1].split(), data[1].split(":")[1].split()
    ):
        time = int(time)
        distance = int(distance)

        for i in range(distance // time, time):
            if i * (time - i) > distance:
                first_win = i
                break

        out *= (time - first_win) - first_win + 1

    return out


def part2(data):
    time = int("".join(time_part for time_part in data[0].split(":")[1].split()))
    distance = int(
        "".join(distance_part for distance_part in data[1].split(":")[1].split())
    )

    for i in range(distance // time, time):
        if i * (time - i) > distance:
            first_win = i
            break

    return (time - first_win) - first_win + 1


measure_performance("part 1", part1, data, unit="microseconds")
print(
    f"Part 2 answer: \033[92m{part2(data)}\x1b[0m. TODO: Optimize. Missing some crucial idea to get it down to microseconds.\n"
)
