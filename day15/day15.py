from performance_utils.performance_utils import measure_performance

with open("day15/in15.txt") as in15:
    data = in15.read().strip()


def hash(s):
    hash = 0
    for c in s:
        hash += ord(c)
        hash *= 17
        hash %= 256

    return hash


def part1(data):
    out = 0

    for instruction in data.split(","):
        out += hash(instruction)

    return out


def part2(data):
    out = 0

    boxes = [{} for _ in range(256)]
    for instruction in data.split(","):
        if instruction[-1] == "-":
            label = instruction[:-1]
            label_hash = hash(label)

            boxes[label_hash].pop(label, None)

        else:
            label, focal_length = instruction.split("=")
            label_hash = hash(label)

            boxes[label_hash][label] = focal_length

    for idx, box in enumerate(boxes):
        for jdx, lens in enumerate(box):
            out += (idx + 1) * (jdx + 1) * int(box[lens])

    return out


measure_performance("part 1", part1, data)
measure_performance("part 2", part2, data)
