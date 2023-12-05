import datetime
import requests
import webbrowser
import os
import argparse

# todo : port past years solution to this repo

parser = argparse.ArgumentParser(description='Initialize Advent of Code day')
parser.add_argument('-d', '--day')
parser.add_argument('-y', '--year')
parser.add_argument('-nb', '--no_browser', action='store_true')
args = parser.parse_args()

session_token = os.environ.get('AOC_SESSION_TOKEN')
if not session_token:
    answer = input('No session token provided; problem input will be missing. Continue? [Y] ')
    if answer.lower() != 'y':
        exit(0)

today = datetime.datetime.now()
year = args.year if args.year else str(today.year)
day = args.day if args.day else today.day

if int(year) > today.year or (int(year) == today.year and int(day) > today.day):
    print("That day hasn't happened yet!")
    exit(0)

if int(day) > 25:
    print("Sorry, that day is after Christmas :(")
    exit(0)


webbrowser.open_new_tab(f"https://adventofcode.com/{year}/day/{day}")

url = f"https://adventofcode.com/{year}/day/{day}/input"
headers = {"Cookie": "session=" + session_token}
day_input = requests.get(url, headers=headers)

try:
    os.mkdir(year)
except:
    pass

parent_dir_path = f"day_{day}"
os.mkdir(os.path.join(year, parent_dir_path))

f = open(os.path.join(year, parent_dir_path, f"day_{day}_input.txt"), "w")
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


f = open(os.path.join(year, parent_dir_path, f"day_{day}.py"), "w")
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


f = open(os.path.join(year, parent_dir_path, f"test_day_{day}.py"), "w")
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

f = open(os.path.join(year, parent_dir_path, f"run_day_{day}.py"), "w")
f.write(RUN_BOILERPLATE)
f.close()
