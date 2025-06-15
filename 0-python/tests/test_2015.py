from year2015.day1 import find_floor
from year2015.day2 import total_wrapping_paper
from year2015.day3 import visited_houses
from year2015.day4 import mining_coins
from year2015.day5 import nice_string
from year2015.day6 import count_lights


def test_day1_1():
    instructions1 = "(())"
    instructions2 = "()()"
    assert find_floor(instructions1) == find_floor(instructions2) == 0


def test_day1_2():
    instructions = "))((((("
    assert find_floor(instructions) == 3


def test_day1_3():
    instructions1 = "())"
    instructions2 = "))("
    assert find_floor(instructions1) == find_floor(instructions2) == -1


def test_day1_4():
    instructions1 = ")))"
    instructions2 = ")())())"
    assert find_floor(instructions1) == find_floor(instructions2) == -3


# ============================================================================


def test_day2_1():
    dimensions = "2x3x4"
    assert total_wrapping_paper(dimensions) == 58


def test_day2_2():
    dimensions = "1x1x10"
    assert total_wrapping_paper(dimensions) == 43


# ============================================================================


def test_day3_1():
    moves = ">"
    assert visited_houses(moves) == 2


def test_day3_2():
    moves = "^>v<"
    assert visited_houses(moves) == 4


def test_day3_3():
    moves = "^v^v^v^v^v"
    assert visited_houses(moves) == 2


# ============================================================================


# def test_day4_1():
#     secret_key = "abcdef"
#     assert mining_coins(secret_key) == 609043


# def test_day4_2():
#     secret_key = "pqrstuv"
#     assert mining_coins(secret_key) == 1048970


# ============================================================================


def test_day5_1():
    input_string = "ugknbfddgicrmopn"
    assert nice_string(input_string) == "nice"


def test_day5_2():
    input_string = "aaa"
    assert nice_string(input_string) == "nice"


def test_day5_3():
    input_string = "jchzalrnumimnmhp"
    assert nice_string(input_string) == "naughty"


def test_day5_4():
    input_string = "haegwjzuvuyypxyu"
    assert nice_string(input_string) == "naughty"


def test_day5_5():
    input_string = "dvszwmarrgswjxmb"
    assert nice_string(input_string) == "naughty"


# ============================================================================


def test_day6_1():
    instructions1 = "turn on 0,0 through 999,999"
    instructions2 = "toggle 0,0 through 999,0"
    instructions3 = "turn off 499,499 through 500,500"

    assert count_lights([instructions1, instructions2, instructions3]) == 998996
