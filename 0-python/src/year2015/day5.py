def nice_string(input_str: str) -> str:
    if (
        condition1(input_str)
        and condition2(input_str)
        and condition3(input_str)
    ):
        return "nice"

    else:
        return "naughty"


def condition1(input_str: str) -> bool:
    counter = 0
    vowels = "aeiou"

    for vowel in vowels:
        counter += input_str.count(vowel)

    if counter >= 3:
        return True

    return False


def condition2(input_str: str) -> bool:
    length = len(input_str) - 1  # to prevent out of index

    for idx in range(length):
        if input_str[idx] == input_str[idx + 1]:
            return True

    return False


def condition3(input_str: str) -> bool:
    patterns = ["ab", "cd", "pq", "xy"]

    for pattern in patterns:
        if pattern in input_str:
            return False

    return True
