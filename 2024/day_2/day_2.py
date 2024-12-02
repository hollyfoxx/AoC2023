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



def solve_problem_1(input: str):
    safe_reports = 0
    for report in helpers.get_lines(input):
        levels = [int(x) for x in report.split()]
        step_direction = levels[0] - levels[1]
        if step_direction > 0:
            report_direction = "dec"
        elif step_direction < 0:
            report_direction = "inc"
        else:
            continue

        safe = True
        for cur, next, pos in helpers.multi_iterate(levels):
            if next is None:
                continue

            step_direction = cur - next
            if abs(step_direction) < 1 or abs(step_direction) > 3:
                safe = False
                break

            if step_direction > 0 and report_direction == "dec":
                continue
            elif step_direction < 0 and report_direction == "inc":
                continue
            else:
                safe = False
                break

        if safe:
            safe_reports += 1

    print(safe_reports)

PROBLEM_2_EXAMPLE__1_ANSWER = 4


def solve_problem_2(input: str):
    safe_reports = 0
    bad_reports = []
    for report in helpers.get_lines(input):
        levels = [int(x) for x in report.split()]

        step_direction = levels[0] - levels[1]
        if step_direction > 0:
            report_direction = "dec"
        elif step_direction < 0:
            report_direction = "inc"
        else:
            bad_reports.append(report)
            continue

        safe = True
        for cur, next, pos in helpers.multi_iterate(levels):
            if next is None:
                continue

            step_direction = cur - next
            if abs(step_direction) < 1 or abs(step_direction) > 3:
                safe = False
                break

            if step_direction > 0 and report_direction == "dec":
                continue
            elif step_direction < 0 and report_direction == "inc":
                continue
            else:
                safe = False
                break

        if safe:
            safe_reports += 1
        else:
            bad_reports.append(report)

    for report in bad_reports:
        levels = [int(x) for x in report.split()]

        for i in range(0, len(levels)):
            modified_levels = levels.copy()
            modified_levels.pop(i)

            step_direction = modified_levels[0] - modified_levels[1]
            if step_direction > 0:
                report_direction = "dec"
            elif step_direction < 0:
                report_direction = "inc"
            else:
                continue

            safe = True
            for cur, next, pos in helpers.multi_iterate(modified_levels):
                if next is None:
                    continue

                step_direction = cur - next
                if abs(step_direction) < 1 or abs(step_direction) > 3:
                    safe = False
                    break

                if step_direction > 0 and report_direction == "dec":
                    continue
                elif step_direction < 0 and report_direction == "inc":
                    continue
                else:
                    safe = False
                    break

            if safe:
                safe_reports += 1
                break
    print(safe_reports)

solve_problem_2(PROBLEM_1_EXAMPLE_1_INPUT)