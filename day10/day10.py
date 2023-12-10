with open("day10/in10.txt") as in10:
    data = [line.strip() for line in in10.readlines()]


def get_grid(data):
    grid = []
    for y, row in enumerate(data):
        grid_row = []
        for x, pipe in enumerate(row):
            if pipe == "|":
                grid_row.append((pipe, (0, -1), (0, 1)))
            elif pipe == "-":
                grid_row.append((pipe, (1, 0), (-1, 0)))
            elif pipe == "L":
                grid_row.append((pipe, (0, -1), (1, 0)))
            elif pipe == "J":
                grid_row.append((pipe, (0, -1), (-1, 0)))
            elif pipe == "7":
                grid_row.append((pipe, (0, 1), (-1, 0)))
            elif pipe == "F":
                grid_row.append((pipe, (1, 0), (0, 1)))
            elif pipe == ".":
                grid_row.append((pipe))
            else:
                grid_row.append((pipe))
                x0 = x
                y0 = y
        grid.append(grid_row)

    return (grid, x0, y0)


def part1(data):
    grid, x0, y0 = get_grid(data)

    if (0, 1) in grid[y0 - 1][x0]:
        xn = x0
        yn = y0 - 1
    elif (-1, 0) in grid[y0][x0 + 1]:
        xn = x0 + 1
        yn = y0
    elif (0, -1) in grid[y0 + 1][x0]:
        xn = x0
        yn = y0 + 1
    else:
        xn = x0 - 1
        yn = y0

    path_length = 1
    visited_nodes = [(xn, yn)]
    while xn != x0 or yn != y0:
        new_xn = xn + grid[yn][xn][1][0]
        new_yn = yn + grid[yn][xn][1][1]

        if (new_xn, new_yn) in visited_nodes:
            new_xn = xn + grid[yn][xn][2][0]
            new_yn = yn + grid[yn][xn][2][1]

        visited_nodes.append((new_xn, new_yn))
        xn = new_xn
        yn = new_yn

        path_length += 1

    return path_length // 2


print(
    f"Part 1 answer: \033[92m{part1(data)}\x1b[0m. Too slow for performance measurement.\n"
)
