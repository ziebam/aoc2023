from math import lcm

from performance_utils.performance_utils import measure_performance

with open("day08/in08.txt") as in08:
    data = [line.strip() for line in in08.readlines()]


def part1(data):
    instructions = data[0]
    len_instructions = len(instructions)

    node_map = {}
    for node in data[2:]:
        start, lr = node.split(" = ")
        l, r = lr.split(", ")
        l = l[1:]
        r = r[:-1]

        node_map[start] = {"L": l, "R": r}

    current_node = "AAA"
    steps = 0
    while current_node != "ZZZ":
        instruction = instructions[steps % len_instructions]
        current_node = node_map[current_node][instruction]
        steps += 1

    return steps


def part2(data):
    instructions = data[0]
    len_instructions = len(instructions)

    node_map = {}
    for node in data[2:]:
        start, lr = node.split(" = ")
        l, r = lr.split(", ")
        l = l[1:]
        r = r[:-1]

        node_map[start] = {"L": l, "R": r}

    nodes = [node for node in node_map.keys() if node.endswith("A")]
    steps_required = []

    for node in nodes:
        num_steps = 0
        next_node = node
        while not next_node.endswith("Z"):
            instruction = instructions[num_steps % len_instructions]
            next_node = node_map[next_node][instruction]
            num_steps += 1
        steps_required.append(num_steps)

    return lcm(*steps_required)


measure_performance("part 1", part1, data)
measure_performance("part 2", part2, data)
