import timeit

with open("day2/in2.txt") as in2:
    data = [line.strip() for line in in2.readlines()]


def part1(data):
    M = {"red": 12, "green": 13, "blue": 14}

    possible_ids = []
    for game in data:
        game_id, subgames = game.split(": ")
        id = int(game_id.split(" ")[-1])

        valid = True
        for subgame in subgames.split("; "):
            for turn in subgame.split(", "):
                n, color = turn.split()
                if int(n) > M[color]:
                    valid = False
                    break
            if not valid:
                break

        if valid:
            possible_ids.append(id)

    return sum(possible_ids)


def part2(data):
    parsed_games = {}
    for game in data:
        game_id, subgames = game.split(": ")
        id = int(game_id.split(" ")[-1])

        parsed_games[id] = {"red": 0, "green": 0, "blue": 0}
        for subgame in subgames.split("; "):
            for subsubgame in subgame.split(", "):
                n, color = subsubgame.split()

                if color == "red" and int(n) > parsed_games[id]["red"]:
                    parsed_games[id]["red"] = int(n)
                if color == "green" and int(n) > parsed_games[id]["green"]:
                    parsed_games[id]["green"] = int(n)
                if color == "blue" and int(n) > parsed_games[id]["blue"]:
                    parsed_games[id]["blue"] = int(n)

    powers = [
        parsed_game["red"] * parsed_game["green"] * parsed_game["blue"]
        for parsed_game in parsed_games.values()
    ]

    return sum(powers)


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
