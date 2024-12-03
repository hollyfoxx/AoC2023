# Day 3 AoC 2023
# f"https://adventofcode.com/2024/day/3"
import re

PROBLEM_1_EXAMPLE_1_INPUT = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
PROBLEM_1_EXAMPLE__1_ANSWER = 161

def eval_mul(mul_exp: str):
    _, exp = mul_exp.split("(")
    exp, _ = exp.split(")")
    x, y = exp.split(",")

    return int(x) * int(y)

def solve_problem_1(input: str):
    mul_expressions = re.finditer(r'mul\(\d{1,3},\d{1,3}\)', input)

    sum = 0
    for mul_exp_group in mul_expressions:
        sum += eval_mul(mul_exp_group.group())

    print(sum)
    return sum

PROBLEM_2_EXAMPLE_1_INPUT = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
PROBLEM_2_EXAMPLE__1_ANSWER = 48


def solve_problem_2(input: str):
    mul_expressions = re.finditer(r'mul\(\d{1,3},\d{1,3}\)|don\'t\(\)|do\(\)', input)

    sum = 0
    mul_instructions_enabled = True
    for mul_exp_group in mul_expressions:
        if mul_exp_group.group() == "don't()":
            mul_instructions_enabled = False

        elif mul_exp_group.group() == "do()":
            mul_instructions_enabled = True

        else:
            if mul_instructions_enabled:
                sum += eval_mul(mul_exp_group.group())

    print(sum)
    return sum
