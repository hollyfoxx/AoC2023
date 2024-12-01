# Day 1 AoC 2023
# f"https://adventofcode.com/2024/day/1"
from typing import List, Tuple

import helpers

PROBLEM_1_EXAMPLE_1_INPUT = """3   4
4   3
2   5
1   3
3   9
3   3"""
PROBLEM_1_EXAMPLE__1_ANSWER = 11


def build_sorted_lists(input) -> Tuple[List[int], List[int]]:
    first = []
    second = []

    for line in helpers.get_lines(input):
        nums = line.split()
        first.append(int(nums[0]))
        second.append(int(nums[1]))

    first = sorted(first)
    second = sorted(second)

    return first, second

def solve_problem_1(input: str):
    first, second = build_sorted_lists(input)

    sum = 0
    for i in range(0, len(first)):
        sum += abs(first[i] - second[i])

    print(sum)
    return sum


PROBLEM_2_EXAMPLE_1_INPUT = PROBLEM_1_EXAMPLE_1_INPUT
PROBLEM_2_EXAMPLE__1_ANSWER = 31


def solve_problem_2(input: str):
    first, second = build_sorted_lists(input)

    sum = 0
    for num in first:
        appearances = second.count(num)
        sum += num * appearances

    print(sum)
