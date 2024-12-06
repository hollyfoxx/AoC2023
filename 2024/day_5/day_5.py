# Day 5 AoC 2023
# f"https://adventofcode.com/2024/day/5"
from typing import Tuple, List

import helpers

PROBLEM_1_EXAMPLE_1_INPUT = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
PROBLEM_1_EXAMPLE__1_ANSWER = 143

def test_update(rule_map, update) -> bool:
    legal_update = True
    seen_pages = set()
    for page in update:
        illegal_pages = rule_map.get(page, set())
        if illegal_pages.intersection(seen_pages):
            legal_update = False
            break

        seen_pages.add(page)

    return legal_update

def sum_middle_pages(updates) -> int:
    sum = 0
    for update in updates:
        middle_index = len(update) // 2
        sum += int(update[middle_index])

    return sum

def solve_problem_1(input: str):
    # {number: every number that must come after it}
    rule_map = {}
    updates = []
    updates_to_print = []

    # Build input maps
    for line in helpers.get_lines(input):
        if "|" in line:
            first, second = line.split("|")
            if first in rule_map:
                rule_map[first].add(second)
            else:
                rule_map[first] = {second}

        else:
            updates.append(line.split(","))

    # Determine which updates to print
    for update in updates:
        print_page = test_update(rule_map, update)
        if print_page:
            updates_to_print.append(update)

    # Sum 'middle' numbers from each update
    sum = sum_middle_pages(updates_to_print)

    print(sum)
    return sum

PROBLEM_2_EXAMPLE__1_ANSWER = 123

def solve_problem_2(input: str):
    # {number: every number that must come after it}
    rule_map = {}
    updates = []
    bad_updates = []

    # Build input maps
    for line in helpers.get_lines(input):
        if "|" in line:
            first, second = line.split("|")
            if first in rule_map:
                rule_map[first].add(second)
            else:
                rule_map[first] = {second}

        else:
            updates.append(line.split(","))

    # Determine which updates to print
    for update in updates:
        print_update = test_update(rule_map, update)
        if not print_update:
            bad_updates.append(update)


    # Correct bad updates
    fixed_updates = []
    for update in bad_updates:
        fixed_update = update
        while not test_update(rule_map, fixed_update):
            seen_pages = set()
            current_i = 0
            for page in update:
                illegal_pages = rule_map.get(page, set())
                bad_page = illegal_pages.intersection(seen_pages)
                if bad_page:
                    bad_page = bad_page.pop()
                    bad_page_i = fixed_update.index(bad_page)
                    fixed_update[current_i] = bad_page
                    fixed_update[bad_page_i] = page
                    break

                current_i += 1
                seen_pages.add(page)

        fixed_updates.append(fixed_update)

    # Sum 'middle' numbers from each update
    sum = sum_middle_pages(fixed_updates)

    print(sum)
    return sum

