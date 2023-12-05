# Day 3 AoC 2023
# f"https://adventofcode.com/2023/day/3"
import re

import helpers

PROBLEM_1_EXAMPLE_1_INPUT = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
PROBLEM_1_EXAMPLE__1_ANSWER = 4361


def solve_problem_1(input: str):
    grid = helpers.Grid(input)

    total = 0
    current_row = 0
    for line in helpers.get_lines(input):
        for match in re.finditer(r'\d+', line):
            for val in grid.get_surrounding_values_span(current_row, match.span()):
                if not val or val in '.0123456789':
                    continue

                total += int(match.group())
                break

        current_row += 1

    print(f"The total of all combined part numbers is: {total}")
    return total


PROBLEM_2_EXAMPLE_1_INPUT = PROBLEM_1_EXAMPLE_1_INPUT
PROBLEM_2_EXAMPLE__1_ANSWER = 467835


def solve_problem_2(input: str):
    grid = helpers.Grid(input)
    gear_map = {}

    total = 0
    current_row = 0
    for line in helpers.get_lines(input):
        for match in re.finditer(r'\d+', line):
            for coord in grid.get_surrounding_coords_span(current_row, match.span()):
                if coord and grid.get_coord_value(coord) == "*":
                    if coord in gear_map:
                        gear_map[coord].append(int(match.group()))

                    else:
                        gear_map[coord] = [int(match.group())]

        current_row += 1

    for gear, part_numbers in gear_map.items():
        if len(part_numbers) == 2:
            total += part_numbers[0] * part_numbers[1]

    print(f"The sum of all gear ratios is {total}")
    return total
