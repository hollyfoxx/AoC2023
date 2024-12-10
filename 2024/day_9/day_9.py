# Day 9 AoC 2023
# f"https://adventofcode.com/2024/day/9"
import re

PROBLEM_1_EXAMPLE_1_INPUT = "12345"
PROBLEM_1_EXAMPLE__1_ANSWER = 60

PROBLEM_1_EXAMPLE_2_INPUT = "2333133121414131402"
PROBLEM_2_EXAMPLE__2_ANSWER = 1928


def solve_problem_1(input: str):
    disk_map = [int(x) for x in input]

    # (file_size, free_space_size)
    file_map = {}

    file_id = 0
    for i in range(0, len(disk_map), 2):
        file_map[file_id] = (disk_map[i], 0)
        if i + 1 < len(disk_map):
            file_map[file_id] = (disk_map[i], disk_map[i + 1])

        file_id += 1

    file_ids = list(file_map.keys())
    print(file_map)
    corrected_disk_map = []
    for file_id in file_map:
        # first fill in file size
        while file_map[file_id][0] > 0:
            corrected_disk_map.append(file_id)
            file_map[file_id] = (file_map[file_id][0] - 1, file_map[file_id][1])

        # then fill in remaining free space
        while file_map[file_id][1] > 0:
            fill_file_id = file_ids[-1]
            if file_map[fill_file_id][0] == 0:
                break

            corrected_disk_map.append(fill_file_id)
            file_map[fill_file_id] = (file_map[fill_file_id][0] - 1, file_map[fill_file_id][1])

            if file_map[fill_file_id][0] == 0:
                file_ids.remove(fill_file_id)

            file_map[file_id] = (file_map[file_id][0], file_map[file_id][1] - 1)

    print(corrected_disk_map)
    sum = 0
    for i, file_id in enumerate(corrected_disk_map):
        sum += i * file_id

    print(sum)
    return sum


PROBLEM_2_EXAMPLE__1_ANSWER = 2858

def solve_problem_2(input: str):
    disk_map = [int(x) for x in input]

    # (file_size, free_space_size)
    file_map = {}

    file_id = 0
    for i in range(0, len(disk_map), 2):
        file_map[file_id] = (disk_map[i], 0)
        if i + 1 < len(disk_map):
            file_map[file_id] = (disk_map[i], disk_map[i + 1])

        file_id += 1

    file_ids = list(file_map.keys())
    corrected_disk_map = []
    for file_id in file_map:
        # first fill in file size
        while file_map[file_id][0] > 0:
            corrected_disk_map.append(file_id)
            file_map[file_id] = (file_map[file_id][0] - 1, file_map[file_id][1])

        # then fill in remaining free space
        while file_map[file_id][1] > 0:
            corrected_disk_map.append(".")
            file_map[file_id] = (file_map[file_id][0], file_map[file_id][1] - 1)

    while file_ids:
        fill_file_id = file_ids.pop()
        print(fill_file_id)
        file_size = corrected_disk_map.count(fill_file_id)
        fill_file_id_start = corrected_disk_map.index(fill_file_id)
        corrected_disk_map_str = ",".join([str(x) for x in corrected_disk_map])
        available_space = re.search(rf"(\.,){{{file_size}}}", corrected_disk_map_str)
        if available_space:
            str_start_index = available_space.start()
            corrected_disk_map_substr = corrected_disk_map_str[:str_start_index]
            start_index = corrected_disk_map_substr.count(",")

            if start_index < fill_file_id_start:
                while fill_file_id in corrected_disk_map:
                    old_index = corrected_disk_map.index(fill_file_id)
                    corrected_disk_map[old_index] = "."

                for i in range(0, file_size):
                    corrected_disk_map[start_index + i] = fill_file_id

        while corrected_disk_map[-1] == ".":
            corrected_disk_map.pop()

    sum = 0
    for i, file_id in enumerate(corrected_disk_map):
        if file_id == ".":
            continue
        sum += i * file_id

    print(sum)
    return sum



# solve_problem_2(PROBLEM_1_EXAMPLE_1_INPUT)
# solve_problem_2(PROBLEM_1_EXAMPLE_2_INPUT)