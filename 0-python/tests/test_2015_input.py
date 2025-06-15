from year2015.day1 import find_floor
from utils import read_input


def test_day1():
    input_str = read_input("src/year2015/day1_input.txt")

    result_floor = find_floor(input_str)
    print(result_floor)  # 138


if __name__ == "__main__":
    test_day1()
