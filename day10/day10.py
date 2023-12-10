# TODO: Doesn't work for some test inputs where the start point is at the outer edge of the grid.

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
                grid_row.append((pipe,))
            else:
                grid_row.append((pipe,))
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


def is_inside_polygon(x, y, vertices):
    """Checks if the point (x, y) is contained within a polygon defined by `corners`.

    Cast a ray towards infinity to the right of the point. If the number of polygon sides
    it crosses is odd, it's within the polygon. Otherwise, it's outside of it.

    When the ray overlaps with the side, it's not counted as a match."""
    j = len(vertices) - 1
    result = False
    for i in range(len(vertices)):
        # Guarding clause to avoid dividing by 0. Additionally, find out whether `y` is between
        # the y values of the side we're checking for an intersection.
        between_y = (vertices[i][1] < y) != (vertices[j][1] < y)
        # Math from:
        # https://web.archive.org/web/20161108113341/https://www.ecse.rpi.edu/Homepages/wrf/Research/Short_Notes/pnpoly.html
        intersects = between_y and (
            x
            < vertices[i][0]
            + (y - vertices[i][1])
            / (vertices[j][1] - vertices[i][1])
            * (vertices[j][0] - vertices[i][0])
        )

        if intersects:
            result = not result
        j = i

    return result


def part2(data):
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

    visited_nodes = [(xn, yn)]
    vertices = []
    while xn != x0 or yn != y0:
        new_xn = xn + grid[yn][xn][1][0]
        new_yn = yn + grid[yn][xn][1][1]

        if (new_xn, new_yn) in visited_nodes:
            new_xn = xn + grid[yn][xn][2][0]
            new_yn = yn + grid[yn][xn][2][1]

        visited_nodes.append((new_xn, new_yn))
        xn = new_xn
        yn = new_yn
        if grid[yn][xn][0] in ["L", "J", "7", "F", "S"]:
            vertices.append((xn, yn))

    out = 0
    for y, row in enumerate(grid):
        for x, _ in enumerate(row):
            if (x, y) not in visited_nodes:
                out += is_inside_polygon(x, y, vertices)
    return out


print(
    f"Part 1 answer: \033[92m{part1(data)}\x1b[0m. Too slow for performance measurement.\n"
)
print(
    f"Part 1 answer: \033[92m{part2(data)}\x1b[0m. Too slow for performance measurement.\n"
)
