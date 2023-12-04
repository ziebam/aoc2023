import timeit

with open("day4/in4.txt") as in4:
    data = in4.readlines()


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
