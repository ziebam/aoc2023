from performance_utils.performance_utils import measure_performance

with open("day09/in09.txt") as in09:
    data = [line.strip() for line in in09.readlines()]


def part1(data):
    out = 0
    histories = [history.split() for history in data]
    for history in histories:
        history = [int(v) for v in history]
        sequences = [history]
        while not all(v == 0 for v in sequences[-1]):
            next_sequence = []
            for idx, value in enumerate(sequences[-1][1:]):
                next_sequence.append(value - sequences[-1][idx])
            sequences.append(next_sequence)

        len_sequences = len(sequences)
        for idx, sequence in enumerate(sequences[-2::-1]):
            sequences[len_sequences - idx - 2].append(
                sequence[-1] + sequences[len_sequences - idx - 1][-1]
            )

        out += sequences[0][-1]

    return out


def part2(data):
    out = 0
    histories = [history.split() for history in data]
    for history in histories:
        history = [int(v) for v in history]
        sequences = [history]
        while not all(v == 0 for v in sequences[-1]):
            next_sequence = []
            for idx, value in enumerate(sequences[-1][1:]):
                next_sequence.append(value - sequences[-1][idx])
            sequences.append(next_sequence)

        len_sequences = len(sequences)
        for idx, sequence in enumerate(sequences[-2::-1]):
            sequences[len_sequences - idx - 2].insert(
                0, sequence[0] - sequences[len_sequences - idx - 1][0]
            )

        out += sequences[0][0]

    return out


measure_performance("part 1", part1, data)
measure_performance("part 2", part2, data)
