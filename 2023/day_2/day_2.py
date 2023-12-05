# Day 2 AoC 2023
# f"https://adventofcode.com/2023/day/2"
import helpers

PROBLEM_1_EXAMPLE_1_INPUT = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

# Games 1, 2, 5
PROBLEM_1_EXAMPLE__1_ANSWER = 8

COLOR_MAPPING = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def solve_problem_1(input: str):
    """
    Which games are possible if the bag contains only  12 red cubes, 13 green cubes, and 14 blue cubes?
    """
    game = 1
    valid_games = []
    for line in helpers.get_lines(input):
        game_is_valid = True
        _, rounds = line.split(": ")
        rounds = rounds.split("; ")
        for round in rounds:
            cubes = round.split(", ")
            for cube_color in cubes:
                count, color = cube_color.split(" ")
                if COLOR_MAPPING[color] < int(count):
                    game_is_valid = False

        if game_is_valid:
            valid_games.append(game)

        game += 1

    result = sum(valid_games)
    print(f"The solution is {result}")
    return result


PROBLEM_2_EXAMPLE_1_INPUT = PROBLEM_1_EXAMPLE_1_INPUT
PROBLEM_2_EXAMPLE__1_ANSWER = 2286


def solve_problem_2(input: str):
    """What is the fewest number of cubes of each color that could have been in the bag to make the game possible?"""
    game_number = 0
    total = 0
    for line in helpers.get_lines(input):
        game_number += 1
        color_counter = {
            "red": [],
            "blue": [],
            "green": []
        }
        _, rounds = line.split(": ")
        rounds = rounds.split("; ")
        for round in rounds:
            cubes = round.split(", ")
            for cube_color in cubes:
                count, color = cube_color.split(" ")
                color_counter[color].append(int(count))

        min_red = max(color_counter["red"])
        min_blue = max(color_counter["blue"])
        min_green = max(color_counter["green"])
        power = min_red * min_blue * min_green
        total += power

    print(f"The total is {total}")
    return total

