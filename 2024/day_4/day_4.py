# Day 4 AoC 2023
# f"https://adventofcode.com/2024/day/4"
from typing import Tuple

import helpers

PROBLEM_1_EXAMPLE_1_INPUT = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
PROBLEM_1_EXAMPLE__1_ANSWER = 18

def count_xmas_from_coord(grid: helpers.Grid, c: Tuple[int, int]) -> int:
    xmas_count = 0

    left, top_left, top, top_right, right, bottom_right, bottom, bottom_left = grid.get_adjacent_values(c, incl_diagonals=True)
    adj_get_coord_methods = [
        (left, "get_left_coord", "get_left_value"),
        (top_left, "get_top_left_coord", "get_top_left_value"),
        (top, "get_top_coord", "get_top_value"),
        (top_right, "get_top_right_coord", "get_top_right_value"),
        (right, "get_right_coord", "get_right_value"),
        (bottom_right, "get_bottom_right_coord", "get_bottom_right_value"),
        (bottom, "get_bottom_coord", "get_bottom_value"),
        (bottom_left, "get_bottom_left_coord", "get_bottom_left_value"),
    ]

    for direction, get_coord_method, get_value_method in adj_get_coord_methods:
        get_coord = getattr(grid, get_coord_method)
        get_value = getattr(grid, get_value_method)
        if direction == "M":
            m_coord = get_coord(c)
            possible_a = get_value(m_coord)
            if possible_a == "A":
                a_coord = get_coord(m_coord)
                possible_s = get_value(a_coord)
                if possible_s == "S":
                    xmas_count += 1

    return xmas_count

def solve_problem_1(input: str):
    xmas_count = 0

    crossword = helpers.Grid(input)
    for coord in crossword.all_coords():
        current = crossword.get_coord_value(coord)
        if current == "X":
            xmas_count += count_xmas_from_coord(crossword, coord)
        else:
            continue

    print(xmas_count)
    return xmas_count

PROBLEM_2_EXAMPLE__1_ANSWER = 9

def count_x_mas_from_coord(grid: helpers.Grid, c: Tuple[int, int]) -> int:
    x_mas_count = 0

    _, top_left, _, top_right, _, bottom_right, _, bottom_left = grid.get_adjacent_values(c, incl_diagonals=True)

    if (top_left == "M" and bottom_right == "S") or (top_left == "S" and bottom_right == "M"):
        if (top_right == "M" and bottom_left == "S") or (top_right == "S" and bottom_left == "M"):
            x_mas_count += 1

    return x_mas_count

def solve_problem_2(input: str):
    x_mas_count = 0

    crossword = helpers.Grid(input)
    for coord in crossword.all_coords():
        current = crossword.get_coord_value(coord)
        if current == "A":
            x_mas_count += count_x_mas_from_coord(crossword, coord)
        else:
            continue

    print(x_mas_count)
    return x_mas_count