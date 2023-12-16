from performance_utils.performance_utils import measure_performance

with open("day16/in16.txt") as in16:
    data = [line.strip() for line in in16.readlines()]


def traverse(origin, direction, grid, energy_map, explored_paths):
    xn = origin[0] + direction[0]
    yn = origin[1] + direction[1]

    while not ((xn >= len(grid[0]) or xn < 0) or (yn >= len(grid) or yn < 0)):
        energy_map[yn][xn] += 1
        current_tile = grid[yn][xn]

        if current_tile == ".":
            xn += direction[0]
            yn += direction[1]

        elif current_tile == "/":
            if (xn, yn, direction[0], direction[1]) in explored_paths:
                break

            explored_paths.append((xn, yn, direction[0], direction[1]))
            if direction == (1, 0):
                direction = (0, -1)
            elif direction == (0, 1):
                direction = (-1, 0)
            elif direction == (-1, 0):
                direction = (0, 1)
            else:
                direction = (1, 0)

            xn += direction[0]
            yn += direction[1]

        elif current_tile == "\\":
            if (xn, yn, direction[0], direction[1]) in explored_paths:
                break

            explored_paths.append((xn, yn, direction[0], direction[1]))
            if direction == (1, 0):
                direction = (0, 1)
            elif direction == (0, 1):
                direction = (1, 0)
            elif direction == (-1, 0):
                direction = (0, -1)
            else:
                direction = (-1, 0)

            xn += direction[0]
            yn += direction[1]

        elif current_tile == "|":
            if direction == (0, 1) or direction == (0, -1):
                xn += direction[0]
                yn += direction[1]
            else:
                if (xn, yn, direction[0], direction[1]) in explored_paths:
                    break

                explored_paths.append((xn, yn, direction[0], direction[1]))
                traverse((xn, yn), (0, -1), grid, energy_map, explored_paths)
                traverse((xn, yn), (0, 1), grid, energy_map, explored_paths)

        else:
            if direction == (1, 0) or direction == (-1, 0):
                xn += direction[0]
                yn += direction[1]
            else:
                if (xn, yn, direction[0], direction[1]) in explored_paths:
                    break

                explored_paths.append((xn, yn, direction[0], direction[1]))
                traverse((xn, yn), (-1, 0), grid, energy_map, explored_paths)
                traverse((xn, yn), (1, 0), grid, energy_map, explored_paths)


def part1(grid):
    energy_map = [[0 for _ in range(len(data[0]))] for _ in range(len(data))]

    traverse((-1, 0), (1, 0), grid, energy_map, [])

    out = 0
    for row in energy_map:
        for node in row:
            if node > 0:
                out += 1

    return out


def part2(grid):
    results = []
    for x in range(len(data[0])):
        energy_map = [[0 for _ in range(len(data[0]))] for _ in range(len(data))]
        traverse((x, -1), (0, 1), grid, energy_map, [])

        result = 0
        for row in energy_map:
            for node in row:
                if node > 0:
                    result += 1

        results.append(result)

    for x in range(len(data[0])):
        energy_map = [[0 for _ in range(len(data[0]))] for _ in range(len(data))]
        traverse((x, len(data)), (0, -1), grid, energy_map, [])

        result = 0
        for row in energy_map:
            for node in row:
                if node > 0:
                    result += 1

        results.append(result)

    for y in range(len(data)):
        energy_map = [[0 for _ in range(len(data[0]))] for _ in range(len(data))]
        traverse((-1, y), (1, 0), grid, energy_map, [])

        result = 0
        for row in energy_map:
            for node in row:
                if node > 0:
                    result += 1

        results.append(result)

    for y in range(len(data)):
        energy_map = [[0 for _ in range(len(data[0]))] for _ in range(len(data))]
        traverse((len(data[0]), y), (-1, 0), grid, energy_map, [])

        result = 0
        for row in energy_map:
            for node in row:
                if node > 0:
                    result += 1

        results.append(result)

    return max(results)


measure_performance("part 1", part1, data)
print(
    f"Part 2 answer: \033[92m{part2(data)}\x1b[0m. Too slow for performance measurement.\n"
)
