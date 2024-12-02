# Day 2 AoC 2023
# f"https://adventofcode.com/2024/day/2"
from typing import List, Tuple

import helpers

PROBLEM_1_EXAMPLE_1_INPUT = '''
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
'''
PROBLEM_1_EXAMPLE__1_ANSWER = 2

def is_report_safe(levels: List[int]) -> bool:
    step_direction = levels[0] - levels[1]
    if step_direction > 0:
        report_direction = "dec"
    elif step_direction < 0:
        report_direction = "inc"
    else:
        return False

    safe = True
    for cur, next, pos in helpers.multi_iterate(levels):
        if next is None:
            continue

        step_direction = cur - next
        step_size = abs(step_direction)
        if step_size < 1 or step_size > 3:
            safe = False
            break

        if step_direction > 0 and report_direction == "dec":
            continue
        elif step_direction < 0 and report_direction == "inc":
            continue
        else:
            safe = False
            break

    return safe

def find_bad_reports(input: str):
    bad_reports = []
    for report in helpers.get_lines(input):
        levels = [int(x) for x in report.split()]
        if not  is_report_safe(levels):
            bad_reports.append(report)

    return bad_reports

def solve_problem_1(input: str):
    reports = helpers.get_all_lines(input)
    bad_reports = find_bad_reports(input)

    safe_reports = len(reports) - len(bad_reports)
    print(safe_reports)
    return safe_reports

PROBLEM_2_EXAMPLE__1_ANSWER = 4


def solve_problem_2(input: str):
    reports = helpers.get_all_lines(input)
    bad_reports = find_bad_reports(input)
    safe_reports = len(reports) - len(bad_reports)

    for report in bad_reports:
        levels = [int(x) for x in report.split()]

        for i in range(0, len(levels)):
            modified_levels = levels.copy()
            modified_levels.pop(i)

            if is_report_safe(modified_levels):
                safe_reports += 1
                break


    print(safe_reports)
    return safe_reports