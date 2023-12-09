# Day 9 AoC 2023
# f"https://adventofcode.com/2023/day/9"
from typing import List

import helpers

PROBLEM_1_EXAMPLE_1_INPUT = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""
PROBLEM_1_EXAMPLE__1_ANSWER = 114

def get_new_history(parsed: List[int]) -> List[int]:
    current_differences = []
    for idx, number in enumerate(parsed):
        if idx + 1 < len(parsed):
            current_differences.append(parsed[idx + 1] - number)

    return current_differences

def solve_problem_1(input: str):
    sum = 0
    for line in helpers.get_lines(input):
        parsed = [int(num) for num in line.split()]
        historical_differences = [parsed]

        while not all(num == 0 for num in historical_differences[-1]):
            historical_differences.append(get_new_history(historical_differences[-1]))

        last = 0
        for historical_entry in reversed(historical_differences):
            last += historical_entry[-1]

        sum += last

    print(f"The sum of all extrapolated values is {sum}")
    return sum


PROBLEM_2_EXAMPLE_1_INPUT = "10 13 16 21 30 45"
PROBLEM_2_EXAMPLE__1_ANSWER = 5


def solve_problem_2(input: str):
    sum = 0
    for line in helpers.get_lines(input):
        parsed = [int(num) for num in line.split()]
        historical_differences = [parsed]

        while not all(num == 0 for num in historical_differences[-1]):
            historical_differences.append(get_new_history(historical_differences[-1]))

        previous = 0
        for historical_entry in reversed(historical_differences):
            previous = historical_entry[0] - previous

        sum += previous

    print(f"The sum of all extrapolated values is {sum}")
    return sum

