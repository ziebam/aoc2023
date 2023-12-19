from performance_utils.performance_utils import measure_performance


def read_input():
    with open("day19/in19.txt") as in19:
        data = in19.read().strip()
        workflows, parts = data.split("\n\n")

        workflows = workflows.split()
        parsed_workflows = {}
        for workflow in workflows:
            name, instructions = workflow.split("{")
            instructions = instructions.strip("}").split(",")
            parsed_workflows[name] = instructions

        parts = parts.split()
        parsed_parts = []
        for part in parts:
            ratings = part.strip().split(",")
            parsed_part = {}
            for rating in ratings:
                category, value = rating.strip("{").strip("}").split("=")
                parsed_part[category] = int(value)
            parsed_parts.append(parsed_part)

        return parsed_workflows, parsed_parts


def is_part_accepted(part, workflows):
    current_workflow = "in"

    while True:
        for instruction in workflows[current_workflow]:
            if instruction == "A":
                return True

            elif instruction == "R":
                return False

            elif len(instruction.split(":")) == 1:
                current_workflow = instruction
                break

            else:
                condition, destination = instruction.split(":")

                category = condition[0]
                operator = condition[1]
                value = int(condition[2:])

                if operator == "<":
                    if part[category] < value:
                        if destination == "A":
                            return True
                        elif destination == "R":
                            return False
                        else:
                            current_workflow = destination
                            break

                else:
                    if part[category] > value:
                        if destination == "A":
                            return True
                        elif destination == "R":
                            return False
                        else:
                            current_workflow = destination
                            break


def part1(workflows, parts):
    out = 0

    for part in parts:
        if is_part_accepted(part, workflows):
            out += part["x"] + part["m"] + part["a"] + part["s"]

    return out


if __name__ == "__main__":
    workflows, parts = read_input()

    measure_performance("part 1", part1, workflows, parts)
