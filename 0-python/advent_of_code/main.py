from year2015.day6 import count_lights


def test_day6_1():
    instructions1 = "turn on 0,0 through 999,999"
    instructions2 = "toggle 0,0 through 999,0"
    instructions3 = "turn off 499,499 through 500,500"

    count_lights([instructions1, instructions2, instructions3])


if __name__ == "__main__":
    test_day6_1()
