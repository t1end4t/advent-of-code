def find_floor(instructions: str) -> int:
    current_floor = 0

    for instruction in instructions:
        if instruction == "(":
            current_floor += 1

        if instruction == ")":
            current_floor += -1

    return current_floor
