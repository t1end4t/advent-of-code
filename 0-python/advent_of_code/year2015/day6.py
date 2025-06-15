import re
from typing import List


def count_lights(instructions: List[str]):
    n_rows, n_cols = 1000, 1000

    light_array = [[1 for col in range(n_cols)] for row in range(n_rows)]

    for instruction in instructions:
        action, coordinate = extract_instruction(instruction)


def excute_action(action: str, state: bool):
    if action == "turn on":
        state = True

    if action == "turn off":
        state = False

    if action == "toggle":
        state = True


def extract_instruction(instruction: str):
    extracted_instruction = []

    actions = ["turn on", "toggle", "turn off"]
    for action in actions:
        if action in instruction:
            extracted_instruction.append(action)
            break

    pattern = r"^\d+,\d+$"
    matches = re.findall(pattern, instruction)

    extracted_instruction.append(matches)

    return extracted_instruction
