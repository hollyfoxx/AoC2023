import datetime
import requests
import webbrowser
import os

session_token = "53616c7465645f5f14d1e79c14dfafa075bdb621038817369a36afd9c4f1fa5e612ae6d6520e18bed3c51a27496fa8b063b0b9df0f161656478789df7cc36c8a"
year = "2023"
today = datetime.datetime.now()
# day = "1"
day = today.day

if int(day) > 25:
    print("Sorry, it's after Christmas :( have fun next year!")
    exit(0)


webbrowser.open_new_tab(f"https://adventofcode.com/{year}/day/{day}")

url = f"https://adventofcode.com/{year}/day/{day}/input"
headers = headers = {"Cookie": "session=" + session_token}
day_input = requests.get(url, headers=headers)

parent_dir_path = f"day_{day}"
os.mkdir(parent_dir_path)

f = open(os.path.join(parent_dir_path, f"day_{day}_input.txt"), "w")
f.write(day_input.text)
f.close()


CODE_BOILERPLATE = f"""# Day {day} AoC 2023
# f"https://adventofcode.com/{year}/day/{day}"

PROBLEM_1_EXAMPLE_1_INPUT = "REPLACE_ME"
PROBLEM_1_EXAMPLE__1_ANSWER = "REPLACE_ME"


def solve_problem_1(input: str):
    raise NotImplementedError()


PROBLEM_2_EXAMPLE_1_INPUT = "REPLACE_ME"
PROBLEM_2_EXAMPLE__1_ANSWER = "REPLACE_ME"


def solve_problem_2(input: str):
    raise NotImplementedError()
"""


f = open(os.path.join(parent_dir_path, f"day_{day}.py"), "w")
f.write(CODE_BOILERPLATE)
f.close()

TEST_BOILERPLATE = f"""import pytest
import day_{day}

@pytest.mark.parametrize(
    "test_input,expected",
    [
        (day_{day}.PROBLEM_1_EXAMPLE_1_INPUT, day_{day}.PROBLEM_1_EXAMPLE__1_ANSWER),
        # (day_{day}.PROBLEM_1_EXAMPLE_1_INPUT, day_{day}.PROBLEM_1_EXAMPLE__1_ANSWER), # ADD YOUR OWN TEST CASES HERE
    ],
)
def test_solve_problem_1(test_input, expected):
    assert day_{day}.solve_problem_1(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (day_{day}.PROBLEM_2_EXAMPLE_1_INPUT, day_{day}.PROBLEM_2_EXAMPLE__1_ANSWER),
        # (day_{day}.PROBLEM_1_EXAMPLE_1_INPUT, day_{day}.PROBLEM_1_EXAMPLE__1_ANSWER), # ADD YOUR OWN TEST CASES HERE
    ],
)
def test_solve_problem_2(test_input, expected):
    assert day_{day}.solve_problem_2(test_input) == expected

"""


f = open(os.path.join(parent_dir_path, f"test_day_{day}.py"), "w")
f.write(TEST_BOILERPLATE)
f.close()


RUN_BOILERPLATE = f"""# Run solution on day {day} input code
# Solution code is responsible for printing solution

import day_{day}

try:
    f = open("day_{day}/day_{day}_input.txt", "r")
    contents = f.read()
    print("Solution 1 Result:")
    day_{day}.solve_problem_1(contents)
    f.close()
except NotImplementedError:
    pass
    
print("\\n")

try:
    f = open("day_{day}/day_{day}_input.txt", "r")
    contents = f.read()
    print("Solution 2 Result:")
    day_{day}.solve_problem_2(contents)
    f.close()
except NotImplementedError:
    pass
"""

f = open(os.path.join(parent_dir_path, f"run_day_{day}.py"), "w")
f.write(RUN_BOILERPLATE)
f.close()
