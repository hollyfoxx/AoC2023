# Day 10 AoC 2023
# f"https://adventofcode.com/2023/day/10"
from typing import Tuple, List

import helpers

PROBLEM_1_EXAMPLE_1_INPUT = """.....
.S-7.
.|.|.
.L-J.
....."""
PROBLEM_1_EXAMPLE__1_ANSWER = 4

PROBLEM_1_EXAMPLE_2_INPUT = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ"""
PROBLEM_1_EXAMPLE__2_ANSWER = 8

LEFT_CONNECTORS = ["-", "L", "F"]
TOP_CONNECTORS = ["|", "7", "F"]
RIGHT_CONNECTORS = ["-", "7", "J"]
BOTTOM_CONNECTORS = ["|", "L", "J"]

# [[LEFT], [TOP], [RIGHT], [BOTTOM]]
COMPLEX_CONNECTOR_MAP = {
    "-": [["L", "F", "-"], [], ["7", "J", "-"], []],
    "|": [[], ["7", "F", "|"], [], ["L", "J", "|"]],
    "L": [[], ["7", "F", "|"], ["-", "J", "7"], []],
    "F": [[], [], ["-", "J", "7"], ["|", "L", "J"]],
    "7": [["-", "L", "F"], [], [], ["|", "L", "J"]],
    "J": [["-", "L", "F"], ["|", "F", "7"], [], []],
}


def get_connector(current_path: List[Tuple[int, int]], coord: Tuple[int, int], grid: helpers.Grid) -> str:
    potential_path_coords = grid.get_adjacent_values(coord)
    current_pipe = grid.get_coord_value(coord)

    if potential_path_coords[0] in LEFT_CONNECTORS and potential_path_coords[0] in COMPLEX_CONNECTOR_MAP[current_pipe][0]:
        left = grid.get_left_coord(coord)
        if left not in current_path:
            return left

    if potential_path_coords[1] in TOP_CONNECTORS and potential_path_coords[1] in COMPLEX_CONNECTOR_MAP[current_pipe][1]:
        top = grid.get_top_coord(coord)
        if top not in current_path:
            return top

    if potential_path_coords[2] in RIGHT_CONNECTORS and potential_path_coords[2] in COMPLEX_CONNECTOR_MAP[current_pipe][2]:
        right = grid.get_right_coord(coord)
        if right not in current_path:
            return right

    if potential_path_coords[3] in BOTTOM_CONNECTORS and potential_path_coords[3] in COMPLEX_CONNECTOR_MAP[current_pipe][3]:
        bottom = grid.get_bottom_coord(coord)
        if bottom not in current_path:
            return bottom

def get_path(start_coord: Tuple[int, int], grid: helpers.Grid) -> List[Tuple[int, int]]:
    a_path_start = None
    b_path_start = None

    potential_path_coords = grid.get_adjacent_values(start_coord)
    if potential_path_coords[0] in LEFT_CONNECTORS:
        a_path_start = grid.get_left_coord(start_coord)

    if potential_path_coords[1] in TOP_CONNECTORS:
        if not a_path_start:
            a_path_start = grid.get_top_coord(start_coord)
        else:
            b_path_start = grid.get_top_coord(start_coord)

    if potential_path_coords[2] in RIGHT_CONNECTORS:
        if not a_path_start:
            a_path_start = grid.get_right_coord(start_coord)
        else:
            b_path_start = grid.get_right_coord(start_coord)

    if potential_path_coords[3] in BOTTOM_CONNECTORS:
        if not a_path_start:
            a_path_start = grid.get_bottom_coord(start_coord)
        else:
            b_path_start = grid.get_bottom_coord(start_coord)

    a_path = [start_coord, a_path_start]
    b_path = [start_coord, b_path_start]

    while True:
        a_path.append(get_connector(a_path, a_path[-1], grid))
        b_path.append(get_connector(b_path, b_path[-1], grid))
        if a_path[-1] == b_path[-1]:
            break

    return [*a_path, *b_path[1:-1]]


def solve_problem_1(input: str):
    grid = helpers.Grid(input)
    num_rows = len(grid.map)

    start = input.index("S")
    start_row = round(start / num_rows) # todo fix incorrect row calculation
    start_coord = (start_row, grid.map[start_row].index("S"))

    path = get_path(start_coord, grid)
    result = len(path) // 2

    print(f"The number of steps along the loop to reach the furthest point is {result}")
    return result


PROBLEM_2_EXAMPLE_1_INPUT = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""
PROBLEM_2_EXAMPLE__1_ANSWER = 4


PROBLEM_2_EXAMPLE_2_INPUT = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ..."""
PROBLEM_2_EXAMPLE__2_ANSWER = 8

def print_loop_path(grid: helpers.Grid, path: List[Tuple[int, int]]):
    counter = 0
    for coord in grid.all_coords():
        if coord in path:
            print(f"P", end=" ")
            counter += 1
        else:
            print(f"*", end=" ")
        if coord[1] == len(grid.map[0]) - 1:
            print()


"""Calculate the area contained within the loop path."""
def solve_problem_2(input: str):
    grid = helpers.Grid(input)
    num_rows = len(grid.map)

    start = input.index("S")
    start_row = round(start / num_rows) # todo fix incorrect row calculation
    print(start_row)
    start_coord = (start_row, grid.map[start_row].index("S"))
    path = get_path(start_coord, grid)

    # odd = inside
    # even = outside
    inside_loop_count = 0
    for coord in grid.all_coords():
        if coord in path:
            continue

        path_cross_count = 0
        left = grid.get_left_coord(coord)
        while left:
            if left in path:
                path_cross_count += 1
            left = grid.get_left_coord(left)

        if path_cross_count % 2 == 0:
            continue

        path_cross_count = 0
        right = grid.get_right_coord(coord)
        while right:
            if right in path:
                path_cross_count += 1
            right = grid.get_right_coord(right)

        if path_cross_count % 2 == 0:
            continue

        inside_loop_count += 1


    # all_coords = list(grid.all_coords())
    #
    # def flood_fill(coord: tuple[int, int]):
    #     if coord not in all_coords:
    #         return
    #
    #     if coord in path:
    #         all_coords.remove(coord)
    #         return
    #
    #     if coord in all_coords:
    #         all_coords.remove(coord)
    #         flood_fill(grid.get_left_coord(coord))
    #         flood_fill(grid.get_top_left_coord(coord))
    #         flood_fill(grid.get_top_coord(coord))
    #         flood_fill(grid.get_top_right_coord(coord))
    #         flood_fill(grid.get_right_coord(coord))
    #         flood_fill(grid.get_bottom_right_coord(coord))
    #         flood_fill(grid.get_bottom_coord(coord))
    #         flood_fill(grid.get_bottom_left_coord(coord))
    #
    # for i in range(0, len(grid.map)):
    #     flood_fill((i, 0))
    #
    # for i in range(0, len(grid.map)):
    #     flood_fill((i, len(grid.map[0]) - 1))
    #
    # for i in range(0, len(grid.map[0])):
    #     flood_fill((0, i))
    #
    # for i in range(0, len(grid.map[0])):
    #     flood_fill((len(grid.map) - 1, i))
    #
    # inside_loop_count = len(all_coords)

    print(f"The area contained within the loop path is {inside_loop_count}")
    return inside_loop_count
