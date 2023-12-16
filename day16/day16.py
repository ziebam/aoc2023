from performance_utils.performance_utils import measure_performance


def read_input():
    with open("day16/in16.txt") as in16:
        data = [line.strip() for line in in16.readlines()]
        return data


def shine_beam(origin, direction, grid, energized_tiles, explored_paths):
    xn = origin[0] + direction[0]
    yn = origin[1] + direction[1]

    while not ((xn >= len(grid[0]) or xn < 0) or (yn >= len(grid) or yn < 0)):
        energized_tiles.add((xn, yn))
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
                shine_beam((xn, yn), (0, -1), grid, energized_tiles, explored_paths)
                shine_beam((xn, yn), (0, 1), grid, energized_tiles, explored_paths)

        else:
            if direction == (1, 0) or direction == (-1, 0):
                xn += direction[0]
                yn += direction[1]
            else:
                if (xn, yn, direction[0], direction[1]) in explored_paths:
                    break

                explored_paths.append((xn, yn, direction[0], direction[1]))
                shine_beam((xn, yn), (-1, 0), grid, energized_tiles, explored_paths)
                shine_beam((xn, yn), (1, 0), grid, energized_tiles, explored_paths)

    return len(energized_tiles)


def part1(grid):
    energized_tiles = set()
    return shine_beam((-1, 0), (1, 0), grid, energized_tiles, [])


def part2(grid):
    # TODO: Optimization idea. Cache that stores the amount of energized tiles after hitting
    # a splitter (`-` or `|`), reused instead of traversing the grid multiple times.
    n_rows, n_cols = (len(grid), len(grid[0]))

    results = []
    for x in range(n_cols):
        energized_tiles = set()
        results.append(shine_beam((x, -1), (0, 1), grid, energized_tiles, []))

        energized_tiles = set()
        results.append(shine_beam((x, n_rows), (0, -1), grid, energized_tiles, []))

    for y in range(n_rows):
        energized_tiles = set()
        results.append(shine_beam((-1, y), (1, 0), grid, energized_tiles, []))

        energized_tiles = set()
        results.append(shine_beam((n_cols, y), (-1, 0), grid, energized_tiles, []))

    return max(results)


if __name__ == "__main__":
    inp = read_input()

    measure_performance("part 1", part1, inp)
    print(
        f"Part 2 answer: \033[92m{part2(inp)}\x1b[0m. Too slow for performance measurement.\n"
    )
