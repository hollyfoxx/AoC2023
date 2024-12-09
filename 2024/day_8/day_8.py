# Day 8 AoC 2023
# f"https://adventofcode.com/2024/day/8"
from typing import Tuple

import helpers
from itertools import combinations

PROBLEM_1_EXAMPLE_1_INPUT = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""
PROBLEM_1_EXAMPLE__1_ANSWER = 14

def calc_slope(coord_a: Tuple[int, int], coord_b:Tuple[int, int]) -> Tuple[int, int]:
    vertical = coord_b[1] - coord_a[1]
    horizontal = coord_b[0] - coord_a[0]
    return horizontal, vertical

def solve_problem_1(input: str):
    m = helpers.Grid(input)
    antenna_map = {}
    unique_antinode_locations = set()

    for coord in m.all_coords():
        val = m.get_coord_value(coord)
        if val != ".":
            if val not in antenna_map:
                antenna_map[val] = [coord]
            else:
                antenna_map[val].append(coord)

    for frequency in antenna_map:
        if len(antenna_map[frequency]) == 1:
            continue

        combos = list(combinations(antenna_map[frequency], 2))
        for c in combos:
            coord_a = c[0]
            coord_b = c[1]
            slope = calc_slope(coord_a, coord_b)
            antinode_a = (coord_b[0] + slope[0], coord_b[1] + slope[1])
            if m.contains_coord(antinode_a):
                unique_antinode_locations.add(antinode_a)

            antinode_b = (coord_a[0] - slope[0], coord_a[1] - slope[1])
            if m.contains_coord(antinode_b):
                unique_antinode_locations.add(antinode_b)

    for coord in unique_antinode_locations:
        m.update_coord_value(coord, "#")

    print(len(unique_antinode_locations))
    return len(unique_antinode_locations)

PROBLEM_2_EXAMPLE__1_ANSWER = 34

def solve_problem_2(input: str):
    m = helpers.Grid(input)
    antenna_map = {}
    unique_antinode_locations = set()

    for coord in m.all_coords():
        val = m.get_coord_value(coord)
        if val != ".":
            if val not in antenna_map:
                antenna_map[val] = [coord]
            else:
                antenna_map[val].append(coord)

    for frequency in antenna_map:
        if len(antenna_map[frequency]) == 1:
            continue

        unique_antinode_locations.update(antenna_map[frequency])
        combos = list(combinations(antenna_map[frequency], 2))
        for c in combos:
            coord_a = c[0]
            coord_b = c[1]
            slope = calc_slope(coord_a, coord_b)
            antinode_a = (coord_b[0] + slope[0], coord_b[1] + slope[1])
            while m.contains_coord(antinode_a):
                unique_antinode_locations.add(antinode_a)
                antinode_a = (antinode_a[0] + slope[0], antinode_a[1] + slope[1])

            antinode_b = (coord_a[0] - slope[0], coord_a[1] - slope[1])
            while m.contains_coord(antinode_b):
                unique_antinode_locations.add(antinode_b)
                antinode_b = (antinode_b[0] - slope[0], antinode_b[1] - slope[1])

    for coord in unique_antinode_locations:
        m.update_coord_value(coord, "#")

    print(len(unique_antinode_locations))
    return len(unique_antinode_locations)

solve_problem_2(PROBLEM_1_EXAMPLE_1_INPUT)
