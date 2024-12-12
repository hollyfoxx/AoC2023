# Day 11 AoC 2023
# f"https://adventofcode.com/2024/day/11"

# PROBLEM_1_EXAMPLE_1_INPUT = "125 17"
PROBLEM_1_EXAMPLE_1_INPUT = "125 17"
PROBLEM_1_EXAMPLE__1_ANSWER = 55312


def blink(stones: list[str]) -> list[str]:
    new_stones = []
    for stone in stones:
        if stone == "0":
            new_stones.append("1")
        elif len(stone) % 2 == 0:
            half_index = len(stone) // 2
            first_half = stone[:half_index]
            while first_half.startswith("0") and len(first_half) > 1:
                first_half = first_half[1:]
            new_stones.append(first_half)

            second_half = stone[half_index:]
            while second_half.startswith("0") and len(second_half) > 1:
                second_half = second_half[1:]
            new_stones.append(second_half)
        else:
            new_stone = str(int(stone) * 2024)
            new_stones.append(new_stone)

    return new_stones

def solve_problem_1(input: str):
    blinks = 25

    stones = input.split()

    total_stones = 0
    for i, stone in enumerate(stones):
        new_stones = [stone]

        for b in range(0, blinks):
            new_stones = blink(new_stones)
            print(len(new_stones))

        total_stones += len(new_stones)

    print(total_stones)
    return total_stones



PROBLEM_2_EXAMPLE__1_ANSWER = "REPLACE_ME"

# def recurse_stone(stone: str, blinks: int) -> int:
#     total_stones = 0
#
#     new_stones = blink([stone])
#     if len(new_stones) > 1:
#         total_stones += 1
#
#     # print(new_stones)
#     # if we have blinks left, need to recurse again
#     if blinks > 1:
#         for stone in new_stones:
#             total_stones += recurse_stone(stone, blinks - 1)
#
#     print(total_stones)
#     return total_stones



# def solve_problem_2(input: str):
#     blinks = 50
#     stones = input.split()
#
#     total_stones = len(stones)
#     for i, stone in enumerate(stones):
#         print(f"stone {i}")
#         total_stones += recurse_stone(stone, blinks)
#
#     print(total_stones)
#     return total_stones


def blink_dict(stones: list[str]) -> dict:
    new_stones = {}
    for stone in stones:
        if stone == "0":
            new_stones.append("1")
        elif len(stone) % 2 == 0:
            half_index = len(stone) // 2
            first_half = stone[:half_index]
            while first_half.startswith("0") and len(first_half) > 1:
                first_half = first_half[1:]
            new_stones.append(first_half)

            second_half = stone[half_index:]
            while second_half.startswith("0") and len(second_half) > 1:
                second_half = second_half[1:]
            new_stones.append(second_half)
        else:
            new_stone = str(int(stone) * 2024)
            new_stones.append(new_stone)

    return new_stones

def recurse_stone(stone: str, blinks: int) -> int:
    # if we have blinks left, need to recurse again
    if blinks > 1:
        stone_map = {}
        for _ in range(0, blinks):
            new_stones = blink([str(stone)])
            for new_stone in new_stones:
                if new_stone in stone_map:
                    stone_map[new_stone] += 1
                else:
                    stone_map[new_stone] = 1




def solve_problem_2(input: str):
    RESULT_MAP = {}


    blinks = 6

    stones = input.split()

    total_stones = 0
    for stone in stones:
        stone_map = {}
        for _ in range(0, blinks):
            new_stones = blink([str(stone)])
            for new_stone in new_stones:
                if new_stone in stone_map:
                    stone_map[new_stone] += 1
                else:
                    stone_map[new_stone] = 1

            print(stone_map)

        break

    # print(RESULT_MAP)

    print(total_stones)
    return total_stones


solve_problem_2(PROBLEM_1_EXAMPLE_1_INPUT)
