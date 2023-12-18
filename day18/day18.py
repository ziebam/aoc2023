from performance_utils.performance_utils import measure_performance


def read_input():
    with open("day18/in18.txt") as in18:
        data = [line.strip() for line in in18.readlines()]
        return data


def get_polygon_area(polygon):
    """Get polygon's area using the Shoelace formula."""
    vertices = zip(polygon, polygon[1:] + [polygon[0]])
    return 0.5 * abs(sum(x0 * y1 - x1 * y0 for ((x0, y0), (x1, y1)) in vertices))


def get_number_of_points(A, b):
    """Get number of points in the polygon using Pick's theorem solved for i + b.

    Pick's theorem: `A = i + b / 2 - 1`, where:

    - `A` = polygon's area

    - `i` = n of points interior to the polygon

    - `b` = n of points on the polygon's boundary

    Solved for `i + b`: i + b = A + b / 2 + 1
    """

    return A + b / 2 + 1


def part1(dig_plan):
    xn = 0
    yn = 0
    boundary = 0
    vertices = [(xn, yn)]
    for instruction in dig_plan:
        direction, length, _ = instruction.split()
        length = int(length)

        boundary += length

        if direction == "U":
            yn -= length

        elif direction == "D":
            yn += length

        elif direction == "L":
            xn -= length

        else:
            xn += length

        vertices.append((xn, yn))

    area = int(get_polygon_area(vertices))
    return int(get_number_of_points(area, boundary))


def part2(dig_plan):
    xn = 0
    yn = 0
    boundary = 0
    vertices = [(xn, yn)]
    for instruction in dig_plan:
        _, _, hex = instruction.split()
        hex = hex.strip("(").strip(")")
        direction = {0: "R", 1: "D", 2: "L", 3: "U"}[int(hex[-1])]
        length = int(hex[1:-1], 16)

        boundary += length

        if direction == "U":
            yn -= length

        elif direction == "D":
            yn += length

        elif direction == "L":
            xn -= length

        else:
            xn += length

        vertices.append((xn, yn))

    area = int(get_polygon_area(vertices))
    return int(get_number_of_points(area, boundary))


if __name__ == "__main__":
    inp = read_input()

    measure_performance("part 1", part1, inp, unit="microseconds")
    measure_performance("part 2", part2, inp, unit="microseconds")
