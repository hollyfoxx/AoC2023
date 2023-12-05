# Day 1 AoC 2023
# f"https://adventofcode.com/2023/day/1"

import regex as re

import helpers

PROBLEM_1_EXAMPLE_1_INPUT = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
PROBLEM_1_EXAMPLE__1_ANSWER = 142
PROBLEM_1_RE = r'\d'


def solve_problem_1(input: str):
    total = 0
    for line in helpers.get_lines(input):
        results = re.findall(PROBLEM_1_RE, line)
        num = int(results[0] + results[-1])
        total += num

    print(f"The total is {total}")
    return total


PROBLEM_2_EXAMPLE_1_INPUT = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
PROBLEM_2_EXAMPLE__1_ANSWER = 281
PROBLEM_2_EXAMPLE_2_INPUT = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
two1nineight"""
PROBLEM_2_EXAMPLE__2_ANSWER = 309
PROBLEM_2_RE = r'\d|one|two|three|four|five|six|seven|eight|nine'

word_mapping = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def solve_problem_2(input: str):
    total = 0
    for line in helpers.get_lines(input):
        results = re.findall(PROBLEM_2_RE, line, overlapped=True)

        if results[0] in word_mapping:
            first = str(word_mapping[results[0]])
        else:
            first = results[0]

        if results[-1] in word_mapping:
            second = str(word_mapping[results[-1]])
        else:
            second = results[-1]

        num = int(first + second)
        total += num

    print(f"The total is {total}")
    return total
