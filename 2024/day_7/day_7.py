# Day 7 AoC 2023
# f"https://adventofcode.com/2024/day/7"
import helpers
from itertools import product

PROBLEM_1_EXAMPLE_1_INPUT = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""
PROBLEM_1_EXAMPLE__1_ANSWER = 3749


def solve_problem_1(input: str):
    missing_operators = ["+", "*"]
    total_sum = 0
    for line in helpers.get_lines(input):
        t, eq = line.split(": ")
        target = int(t)
        missing_operator_count = eq.count(" ")
        equation = [int(x) for x in eq.split()]
        combos = product(missing_operators, repeat=missing_operator_count)
        for combo in combos:
            result = equation[0]
            for current, next, pos in helpers.multi_iterate(equation):
                if next is None:
                    continue
                if combo[pos] == "+":
                    result += next
                else:
                    result *= next

            if result == target:
                total_sum += target
                break


    print(total_sum)
    return total_sum



PROBLEM_2_EXAMPLE__1_ANSWER = 11387


def solve_problem_2(input: str):
    missing_operators = [ "+", "||", "*", ]
    total_sum = 0
    for line in helpers.get_lines(input):
        t, eq = line.split(": ")
        target = int(t)
        missing_operator_count = eq.count(" ")
        equation = eq.split()
        combos = product(missing_operators, repeat=missing_operator_count)

        for combo in combos:
            new_equation = []
            for num, next_num, pos in helpers.multi_iterate(equation):
                new_equation.append(num)
                if pos == len(equation) - 1:
                    break
                new_equation.append(combo[pos])

            result = int(new_equation[0])
            for index, current in enumerate(new_equation):
                if current in ["+", "*", "||"]:
                    continue

                if index == len(new_equation) - 1:
                    break

                operator = new_equation[index + 1]

                if operator == "+":
                    result += int(new_equation[index + 2])
                elif operator == "*":
                    result *= int(new_equation[index + 2])
                elif operator == "||":
                    result  = int(str(result) + new_equation[index + 2])
                    new_equation[index + 2] = str(result) + new_equation[index + 2]

            if result == target:
                total_sum += target
                break

    print(total_sum)
    return total_sum

solve_problem_2(PROBLEM_1_EXAMPLE_1_INPUT)
