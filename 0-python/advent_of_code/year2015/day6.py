import re
from typing import List, Tuple


def count_lights(instructions: List[str]) -> int:
    lit_lights = 0  # prevent unbound
    n_rows, n_cols = 1000, 1000

    light_array = [[0 for _ in range(n_cols)] for _ in range(n_rows)]

    for instruction in instructions:
        lit_lights = 0

        action, coordinate1, coordinate2 = extract_instruction(instruction)

        # now extract coordinate
        for x in range(coordinate1[0], coordinate2[0] + 1):
            for y in range(coordinate1[1], coordinate2[1] + 1):
                light_array[y][x] = excute_action(
                    action, current_state=light_array[y][x]
                )

        for x in range(n_cols):
            for y in range(n_rows):
                if light_array[y][x] == 1:
                    lit_lights += 1

        print(f"Current have {lit_lights} lights is on")

    return lit_lights


def excute_action(action: str, current_state: int) -> int:
    if action == "turn on":
        return 1

    elif action == "turn off":
        return 0

    else:
        return 1 - current_state


def extract_instruction(
    instruction: str,
) -> Tuple[str, Tuple[int, int], Tuple[int, int]]:
    actions = ["turn on", "toggle", "turn off"]
    action = next((a for a in actions if a in instruction), None)

    if action is None:
        raise ValueError("No valid action found in instruction")

    coordinates = re.findall(r"\d+,\d+", instruction)
    if len(coordinates) != 2:
        raise ValueError(
            "Instruction must contain exactly two coordinate pairs"
        )

    x1, y1 = map(int, coordinates[0].split(","))
    x2, y2 = map(int, coordinates[1].split(","))

    return action, (x1, y1), (x2, y2)
