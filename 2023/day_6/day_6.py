# Day 6 AoC 2023
# f"https://adventofcode.com/2023/day/6"
import math

import helpers

PROBLEM_1_EXAMPLE_1_INPUT = """Time:      7  15   30
Distance:  9  40  200"""
PROBLEM_1_EXAMPLE__1_ANSWER = 288


def solve_problem_1(input: str):
    """
    Calculate the product of number of ways to win each race

    distance = (button_time)(time_to_race - button_time)
    """

    lines = helpers.get_all_lines(input)
    _, times = lines[0].split(":")
    times = times.split()
    _, distances = lines[1].split(":")
    distances = distances.split()

    races = zip(times, distances)

    ways_to_win_per_race = []
    for race in races:
        ways_to_win = 0
        time_to_race = int(race[0])
        distance_high_score = int(race[1])
        for button_time in range(1, time_to_race):
            distance = button_time * (time_to_race - button_time)
            if distance > distance_high_score:
                ways_to_win += 1

        ways_to_win_per_race.append(ways_to_win)

    result = math.prod(ways_to_win_per_race)
    print(f"The total product of ways to win is {result}")
    return result


PROBLEM_2_EXAMPLE_1_INPUT = PROBLEM_1_EXAMPLE_1_INPUT
PROBLEM_2_EXAMPLE__1_ANSWER = 71503


def solve_problem_2(input: str):
    lines = helpers.get_all_lines(input)
    _, times = lines[0].split(":")
    time = times.replace(" ", "")
    _, distances = lines[1].split(":")
    distance = distances.replace(" ", "")

    ways_to_win = 0
    time_to_race = int(time)
    distance_high_score = int(distance)
    for button_time in range(1, time_to_race):
        distance = button_time * (time_to_race - button_time)
        if distance > distance_high_score:
            ways_to_win += 1

    print(f"The total number of ways to win is {ways_to_win}")
    return ways_to_win
