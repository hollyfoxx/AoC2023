# Day 1 AoC 2023
# f"https://adventofcode.com/2020/day/1"

PROBLEM_1_EXAMPLE_1_INPUT = """1721
979
366
299
675
1456"""
PROBLEM_1_EXAMPLE__1_ANSWER = 514579


def solve_problem_1(input: str):
    expenses = [int(x) for x in input.split('\n')]
    for i_expense in expenses:
        for j_expense in expenses:
            if i_expense + j_expense == 2020:
                return i_expense * j_expense


PROBLEM_2_EXAMPLE_1_INPUT = PROBLEM_1_EXAMPLE_1_INPUT
PROBLEM_2_EXAMPLE__1_ANSWER = 241861950


def solve_problem_2(input: str):
    expenses = [int(x) for x in input.split('\n')]
    for i_expense in expenses:
        for j_expense in expenses:
            for k_expense in expenses:
                if i_expense + j_expense + k_expense == 2020:
                    return i_expense * j_expense * k_expense
