from performance_utils.performance_utils import measure_performance

with open("day04/in04.txt") as in04:
    data = in04.readlines()


def part1(data):
    out = 0

    for line in data:
        winning_numbers, numbers = (n.split() for n in line.split(":")[1].split(" | "))

        winning = 0
        for number in numbers:
            if number in winning_numbers:
                winning += 1

        out += 2 ** (winning - 1) if winning else 0

    return out


def part2(data):
    counts = [1 for _ in data]

    for idx, line in enumerate(data):
        winning_numbers, numbers = (n.split() for n in line.split(":")[1].split(" | "))

        winning = 0
        for number in numbers:
            if number in winning_numbers:
                winning += 1

        for i in range(idx + 1, idx + 1 + winning):
            counts[i] += counts[idx]

    return sum(counts)


measure_performance("part 1", part1, data)
measure_performance("part 2", part2, data)
