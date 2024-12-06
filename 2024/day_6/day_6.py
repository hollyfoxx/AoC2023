# Day 6 AoC 2023
# f"https://adventofcode.com/2024/day/6"
from typing import Tuple

import helpers

PROBLEM_1_EXAMPLE_1_INPUT = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
PROBLEM_1_EXAMPLE__1_ANSWER = 41

def find_guard(grid: helpers.Grid) -> Tuple[int, int]:
    for coord in grid.all_coords():
        if grid.get_coord_value(coord) in ["^", "<", ">", "v"]:
            return coord

def guard_step(grid: helpers.Grid, current_pos: Tuple[int, int]) -> Tuple[helpers.Grid, Tuple[int, int]]:
    directions = ["top", "right", "bottom", "left", "top", "right"]
    direction_symbols =  ["^", ">", "v", "<", "^", ">",]
    current_direction = direction_symbols.index(grid.get_coord_value(current_pos))

    turns = 0
    for direction in directions[current_direction:]:
        get_direction_coord = getattr(grid, f"get_{direction}_coord")
        get_direction_value = getattr(grid, f"get_{direction}_value")
        if get_direction_value(current_pos) not in  ["#", "O"]:
            new_direction_index = direction_symbols.index(grid.get_coord_value(current_pos)) + turns
            grid.update_coord_value(current_pos, "X")
            grid.update_coord_value(get_direction_coord(current_pos), direction_symbols[new_direction_index])
            return grid, get_direction_coord(current_pos)

        turns += 1
        if turns == 4:
            raise Exception("The guard is trapped :(")

def solve_problem_1(input: str):
    lab_map = helpers.Grid(input)
    guard_pos = find_guard(lab_map)

    while True:
        try:
            lab_map, guard_pos = guard_step(lab_map, guard_pos)

        # Will get a TypeError when guard goes off map
        except TypeError:
            break

    positions = [pos for row in lab_map.map for pos in row]
    unique_positions = positions.count("X")
    print(unique_positions)
    return unique_positions


PROBLEM_2_EXAMPLE__1_ANSWER = 6


def solve_problem_2(input: str):
    original_lab_map = helpers.Grid(input)
    guard_start = find_guard(original_lab_map)
    obstacle_positions = 0

    for coord in original_lab_map.all_coords():
        print(coord)
        lab_map = helpers.Grid(input)
        if lab_map.get_coord_value(coord) not in ["^", "#"]:
            obstacle_hit_map = {}
            lab_map.update_coord_value(coord, "O")

            for obs in lab_map.all_coords():
                if lab_map.get_coord_value(obs) in ["O", "#"]:
                    left, top, right, bottom = lab_map.get_adjacent_coords(obs)
                    obstacle_hit_map.update({
                        top: 0,
                        left: 0,
                        bottom: 0,
                        right: 0
                    })
        else:
            continue


        guard_pos = guard_start
        while True:
            try:
                lab_map, guard_pos = guard_step(lab_map, guard_pos)
                if guard_pos in obstacle_hit_map:
                    if obstacle_hit_map[guard_pos] > 2:
                        obstacle_positions += 1
                        print(obstacle_positions)
                        break
                    else:
                        obstacle_hit_map[guard_pos] += 1

            # Will get a TypeError when guard goes off map
            except TypeError:
                break

    print(obstacle_positions)
    return obstacle_positions
