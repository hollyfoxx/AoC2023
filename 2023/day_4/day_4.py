# Day 4 AoC 2023
# f"https://adventofcode.com/2023/day/4"
from typing import Union

import helpers


def get_matches(line: str) -> Union[None, int]:
    _, numbers = line.split(": ")
    winning, our_numbers = numbers.split(" | ")

    winning = set([int(num) for num in winning.split()])
    our_numbers = set([int(num) for num in our_numbers.split()])

    matches = our_numbers.intersection(winning)
    if matches:
        return len(matches)

    return None


PROBLEM_1_EXAMPLE_1_INPUT = """"Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
PROBLEM_1_EXAMPLE__1_ANSWER = 13


def solve_problem_1(input: str):
    total = 0
    for line in helpers.get_lines(input):
        num_matches = get_matches(line)
        if num_matches:
            total += 2 ** (num_matches - 1)

    print(f"The total number of points is {total}")
    return total


PROBLEM_2_EXAMPLE_1_INPUT = PROBLEM_1_EXAMPLE_1_INPUT
PROBLEM_2_EXAMPLE__1_ANSWER = 30


def solve_problem_2(input: str):
    starting_number_of_cards = len(input.split("\n")) + 1
    card_tracker = {i: 1 for i in range(1, starting_number_of_cards)}

    current_card = 1
    for line in helpers.get_lines(input):
        copies_current_card = card_tracker[current_card]

        num_matches = get_matches(line)
        if num_matches:
            for i in range(current_card + 1, current_card + 1 + num_matches):
                if i not in card_tracker:
                    break
                card_tracker[i] += copies_current_card

        current_card += 1

    total_ending_cards = sum(card_tracker.values())
    print(f"The total number of scratchcards is {total_ending_cards}")
    return total_ending_cards
