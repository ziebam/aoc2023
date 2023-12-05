from performance_utils.performance_utils import measure_performance

with open("day5/in5.txt") as in5:
    data = [line.strip() for line in in5.readlines() if len(line.strip())]


def part1(data):
    seeds = [int(seed) for seed in data[0].split(": ")[1].split()]

    maps = {}
    for line in data[1:]:
        if "map" in line:
            source, _, dest = line.split()[0].split("-")
            maps[source] = [
                dest,
            ]
        else:
            maps[source] += [[int(num) for num in line.split()]]

    seed_to_location = {}
    for seed in seeds:
        next_step = seed
        for map in maps:
            for instruction in maps[map][1:]:
                dest_range_start, source_range_start, range_length = instruction
                if (
                    next_step >= source_range_start
                    and next_step < source_range_start + range_length
                ):
                    next_step += dest_range_start - source_range_start
                    break
        seed_to_location[seed] = next_step

    return min(seed_to_location.values())


def part2(data):
    seeds_ranges = [int(n) for n in data[0].split(": ")[1].split()]
    for i in range(1, len(seeds_ranges), 2):
        seeds_ranges[i] += seeds_ranges[i - 1]

    maps = {}
    for line in data[1:]:
        if "map" in line:
            source, _, dest = line.split()[0].split("-")
            maps[source] = [
                dest,
            ]
        else:
            maps[source] += [[int(num) for num in line.split()]]

    max_location = None
    for dest_range_start, _, range_length in maps["humidity"][1:]:
        if max_location is None:
            max_location = dest_range_start + range_length
        elif dest_range_start + range_length > max_location:
            max_location = dest_range_start + range_length

    current_location = 0
    while current_location < max_location:
        next_step = current_location
        for map in list(maps)[::-1]:
            for instruction in maps[map][1:]:
                # Reverse the approach from part 1.
                source_range_start, dest_range_start, range_length = instruction
                if (
                    next_step >= source_range_start
                    and next_step < source_range_start + range_length
                ):
                    next_step += dest_range_start - source_range_start
                    break

        for idx, min_seeds_range in enumerate(seeds_ranges):
            if idx % 2 == 1:
                continue
            if next_step >= min_seeds_range and next_step < seeds_ranges[idx + 1]:
                return current_location

        current_location += 1


measure_performance("part 1", part1, data)
print(
    f"Part 2 answer: \033[92m{part2(data)}\x1b[0m. No time measurement since it takes a few minutes.\n"
)
