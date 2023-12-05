# Day 3 AoC 2023
# f"https://adventofcode.com/2020/day/3"

PROBLEM_1_EXAMPLE_1_INPUT = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""
PROBLEM_1_EXAMPLE__1_ANSWER = 7


def solve_problem_1(input: str):
    tree_map = input.split("\n")
    pattern_length = len(tree_map[0])

    tree_count = 0
    x_index = 0
    for y_index in range(0, len(tree_map)):
        if y_index == 0:
            continue

        x_index += 3
        if x_index > pattern_length - 1:
            x_index -= pattern_length

        if tree_map[y_index][x_index] == "#":
            tree_count += 1

    return tree_count


PROBLEM_2_EXAMPLE_1_INPUT = PROBLEM_1_EXAMPLE_1_INPUT
PROBLEM_2_EXAMPLE__1_ANSWER = 336


def solve_problem_2(input: str):
    tree_map = input.split("\n")
    pattern_length = len(tree_map[0])

    tree_counts = []
    for x_step in [1, 3, 5, 7]:
        tree_count = 0
        x_index = 0
        for y_index in range(0, len(tree_map)):
            if y_index == 0:
                continue

            x_index += x_step
            if x_index > pattern_length - 1:
                x_index -= pattern_length

            if tree_map[y_index][x_index] == "#":
                tree_count += 1

        tree_counts.append(tree_count)

    tree_count = 0
    x_index = 0
    for y_index in range(0, len(tree_map), 2):
        if y_index == 0:
            continue

        x_index += 1
        if x_index > pattern_length - 1:
            x_index -= pattern_length

        if tree_map[y_index][x_index] == "#":
            tree_count += 1

    tree_counts.append(tree_count)

    product = 1
    for count in tree_counts:
        product *= count

    return product
