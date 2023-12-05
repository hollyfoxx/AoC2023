# Day 2 AoC 2023
# f"https://adventofcode.com/2020/day/2"

PROBLEM_1_EXAMPLE_1_INPUT = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""
PROBLEM_1_EXAMPLE__1_ANSWER = 2


def solve_problem_1(input: str):
    entries = input.split("\n")

    valid_passwords = 0
    for entry in entries:
        policy, password = entry.split(": ")
        letter_limits, letter = policy.split(" ")
        minimum, maximum = letter_limits.split("-")

        password_letter_count = password.count(letter)
        if int(minimum) <= password_letter_count <= int(maximum):
            valid_passwords += 1

    return valid_passwords


PROBLEM_2_EXAMPLE_1_INPUT = PROBLEM_1_EXAMPLE_1_INPUT
PROBLEM_2_EXAMPLE__1_ANSWER = 1


def solve_problem_2(input: str):
    entries = input.split("\n")

    valid_passwords = 0
    for entry in entries:
        policy, password = entry.split(": ")
        indexes, letter = policy.split(" ")
        first_index, last_index = [int(x) for x in indexes.split("-")]

        # push space at beginning of pw to account for index starting at 1
        password = f" {password}"
        if (
                password[first_index] == letter and not password[last_index] == letter
        ) or (
                not password[first_index] == letter and password[last_index] == letter
        ):
            valid_passwords += 1

    return valid_passwords
