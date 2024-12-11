# Day 10 AoC 2023
# f"https://adventofcode.com/2024/day/10"
from typing import Tuple

import helpers

PROBLEM_1_EXAMPLE_1_INPUT = """0123
1234
8765
9876"""
PROBLEM_1_EXAMPLE__1_ANSWER = 1

PROBLEM_1_EXAMPLE_2_INPUT = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
PROBLEM_1_EXAMPLE__2_ANSWER = 36

PROBLEM_1_EXAMPLE_3_INPUT = """..90..9
...1.98
...2..7
6543456
765.987
876....
987...."""
PROBLEM_1_EXAMPLE__3_ANSWER = 4

def get_valid_steps(topo_map: helpers.Grid, coord: Tuple[int, int]) -> list[Tuple[int, int]]:
    steps = []
    left, top, right, bottom = topo_map.get_adjacent_values(coord)
    if left and left != "." and int(left) == int(topo_map.get_coord_value(coord)) + 1:
        steps.append(topo_map.get_left_coord(coord))

    if top and top != "." and int(top) == int(topo_map.get_coord_value(coord)) + 1:
        steps.append(topo_map.get_top_coord(coord))

    if right and right != "." and int(right) == int(topo_map.get_coord_value(coord)) + 1:
        steps.append(topo_map.get_right_coord(coord))

    if bottom and bottom != "." and int(bottom) == int(topo_map.get_coord_value(coord)) + 1:
        steps.append(topo_map.get_bottom_coord(coord))

    return steps

def get_trail(topo_map: helpers.Grid, steps: list[Tuple[int, int]]) -> list[tuple[int, int]]:
    if topo_map.get_coord_value(steps[-1]) == "9":
        return steps

    next_steps = get_valid_steps(topo_map, steps[-1])
    for step in next_steps:
        new_trail = [*steps, step]
        return get_trail(topo_map, new_trail)

def solve_problem_1(input: str):
    topo_map = helpers.Grid(input)
    possible_trailheads = {}

    for coord in topo_map.all_coords():
        if topo_map.get_coord_value(coord) == "0":
            possible_trailheads[coord] = 0

    for trailhead in possible_trailheads:
        current_trails = [[trailhead]]
        while True:
            new_trails = []
            for trail in current_trails:
                next_steps = get_valid_steps(topo_map, trail[-1])
                for step in next_steps:
                    new_trail = [*trail, step]
                    new_trails.append(new_trail)

            if not new_trails:
                break
            current_trails = new_trails

        unique_peaks = set()
        for trail in current_trails:
            unique_peaks.add(trail[-1])

        possible_trailheads[trailhead] = len(unique_peaks)

    topo_map.pretty_print()

    print(sum(possible_trailheads.values()))
    return sum(possible_trailheads.values())

# solve_problem_1(PROBLEM_1_EXAMPLE_1_INPUT)
# solve_problem_1(PROBLEM_1_EXAMPLE_2_INPUT)
# solve_problem_1(PROBLEM_1_EXAMPLE_3_INPUT)

PROBLEM_2_EXAMPLE__1_INPUT = """..90..9
...1.98
...2..7
6543456
765.987
876....
987...."""
PROBLEM_2_EXAMPLE__1_ANSWER = 13

PROBLEM_2_EXAMPLE__2_INPUT = """012345
123456
234567
345678
4.6789
56789."""
PROBLEM_2_EXAMPLE__2_ANSWER = 227

PROBLEM_2_EXAMPLE__3_INPUT = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
PROBLEM_2_EXAMPLE__3_ANSWER = 81


def solve_problem_2(input: str):
    topo_map = helpers.Grid(input)
    possible_trailheads = {}

    for coord in topo_map.all_coords():
        if topo_map.get_coord_value(coord) == "0":
            possible_trailheads[coord] = 0

    for trailhead in possible_trailheads:
        current_trails = [[trailhead]]
        while True:
            new_trails = []
            for trail in current_trails:
                next_steps = get_valid_steps(topo_map, trail[-1])
                for step in next_steps:
                    new_trail = [*trail, step]
                    new_trails.append(new_trail)

            if not new_trails:
                break
            current_trails = new_trails

        possible_trailheads[trailhead] = len(current_trails)

    topo_map.pretty_print()

    print(sum(possible_trailheads.values()))
    return sum(possible_trailheads.values())

# solve_problem_2(PROBLEM_2_EXAMPLE__1_INPUT)
# solve_problem_2(PROBLEM_2_EXAMPLE__2_INPUT)
# solve_problem_2(PROBLEM_2_EXAMPLE__3_INPUT)