# Day 8 AoC 2023
# f"https://adventofcode.com/2023/day/8"
import math

import helpers

PROBLEM_1_EXAMPLE_1_INPUT = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""
PROBLEM_1_EXAMPLE__1_ANSWER = 2
PROBLEM_1_EXAMPLE_2_INPUT = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""
PROBLEM_1_EXAMPLE__2_ANSWER = 6


def solve_problem_1(input: str):
    lines = helpers.get_all_lines(input)
    sequence = lines[0]
    network_map = {}
    for line in lines:
        if line == sequence:
            continue

        node, fork = line.split(" = ")
        fork = fork.replace("(", "('").replace(")", "')").replace(", ", "', '")
        network_map[node] = eval(fork)

    steps = 0
    current = "AAA"
    while True:
        for s in sequence:
            if s == "L":
                current = network_map[current][0]
            elif s == "R":
                current = network_map[current][1]

            steps += 1
            if current == "ZZZ":
                break

        if current == "ZZZ":
            break

    print(f"The number of steps required to reach the end is {steps}")
    return steps


PROBLEM_2_EXAMPLE_1_INPUT = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""
PROBLEM_2_EXAMPLE__1_ANSWER = 6


def solve_problem_2(input: str):
    lines = helpers.get_all_lines(input)
    sequence = lines[0]
    network_map = {}
    for line in lines:
        if line == sequence:
            continue

        node, fork = line.split(" = ")
        fork = fork.replace("(", "('").replace(")", "')").replace(", ", "', '")
        network_map[node] = eval(fork)

    starting_nodes = [node for node in network_map.keys() if node[-1] == "A"]
    each_steps = []
    for current in starting_nodes:
        steps = 0
        at_the_end = False
        while True:
            for s in sequence:
                if s == "L":
                    current = network_map[current][0]
                elif s == "R":
                    current = network_map[current][1]

                steps += 1
                if current[-1] == "Z":
                    at_the_end = True
                    break

            if at_the_end:
                each_steps.append(steps)
                break

    result = math.lcm(*each_steps)
    print(f"The number of steps required to reach the end is {result}")
    return result
