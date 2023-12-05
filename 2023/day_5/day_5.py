# Day 5 AoC 2023
# f"https://adventofcode.com/2023/day/5"
from typing import Tuple, List
from tqdm import tqdm

import helpers

PROBLEM_1_EXAMPLE_1_INPUT = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""
PROBLEM_1_EXAMPLE__1_ANSWER = 35

def build_map(almanac: List[str], map_key: str) -> List[Tuple[int, int, int]]:
    index = almanac.index(map_key)
    current = index + 1
    mapping = []
    while True:
        if current == len(almanac):
            break

        if "map" in almanac[current]:
            break

        instruction = [int(num) for num in almanac[current].split()]
        mapping.append((instruction[0], instruction[1], instruction[1] + instruction[2] - 1))
        current += 1

    return mapping


def lookup_mapping(mapping: List[Tuple[int, int, int]], lookup_value: int) -> int:
    corresponding = lookup_value
    for dst, lower, upper in mapping:
        if lower <= lookup_value <= upper:
            difference = lookup_value - lower
            corresponding = dst + difference

    return corresponding

def solve_problem_1(input: str):
    almanac = helpers.get_all_lines(input)
    _, seeds = almanac[0].split(": ")
    seeds = [int(seed) for seed in seeds.split()]

    seed_to_soil_map = build_map(almanac,  "seed-to-soil map:")
    soil_to_fertilizer_map = build_map(almanac,  "soil-to-fertilizer map:")
    fertilizer_to_water_map = build_map(almanac,  "fertilizer-to-water map:")
    water_to_light_map = build_map(almanac,  "water-to-light map:")
    light_to_temperature_map = build_map(almanac,  "light-to-temperature map:")
    temperature_to_humidity_map = build_map(almanac,  "temperature-to-humidity map:")
    humidity_to_location_map = build_map(almanac,  "humidity-to-location map:")

    locations = []
    for seed in seeds:
        soil = lookup_mapping(seed_to_soil_map, seed)
        fertilizer = lookup_mapping(soil_to_fertilizer_map, soil)
        water = lookup_mapping(fertilizer_to_water_map, fertilizer)
        light = lookup_mapping(water_to_light_map, water)
        temperature = lookup_mapping(light_to_temperature_map, light)
        humidity = lookup_mapping(temperature_to_humidity_map, temperature)
        location = lookup_mapping(humidity_to_location_map, humidity)
        locations.append(location)

    lowest = min(locations)
    print(f"The lowest location number is {lowest}")
    return lowest


PROBLEM_2_EXAMPLE_1_INPUT = PROBLEM_1_EXAMPLE_1_INPUT
PROBLEM_2_EXAMPLE__1_ANSWER = 46


def solve_problem_2(input: str):
    almanac = helpers.get_all_lines(input)
    _, seed_numbers = almanac[0].split(": ")
    seed_numbers = [int(seed) for seed in seed_numbers.split()]
    seed_pairs = []
    for i in range(0, len(seed_numbers) - 1, 2):
        seed_pairs.append((seed_numbers[i], seed_numbers[i + 1]))

    seed_to_soil_map = build_map(almanac,  "seed-to-soil map:")
    soil_to_fertilizer_map = build_map(almanac,  "soil-to-fertilizer map:")
    fertilizer_to_water_map = build_map(almanac,  "fertilizer-to-water map:")
    water_to_light_map = build_map(almanac,  "water-to-light map:")
    light_to_temperature_map = build_map(almanac,  "light-to-temperature map:")
    temperature_to_humidity_map = build_map(almanac,  "temperature-to-humidity map:")
    humidity_to_location_map = build_map(almanac,  "humidity-to-location map:")

    locations = []
    # print(len(seed_pairs))
    # print(seed_pairs[6])
    for index, pair in enumerate(seed_pairs):
        if index != 9:
            continue
        # lower = pair[0]
        # upper = pair[0] + pair[1]
        # average = (lower + upper) / 2
        for s in tqdm(range(pair[0], pair[0] + pair[1])):
            soil = lookup_mapping(seed_to_soil_map, s)
            fertilizer = lookup_mapping(soil_to_fertilizer_map, soil)
            water = lookup_mapping(fertilizer_to_water_map, fertilizer)
            light = lookup_mapping(water_to_light_map, water)
            temperature = lookup_mapping(light_to_temperature_map, light)
            humidity = lookup_mapping(temperature_to_humidity_map, temperature)
            location = lookup_mapping(humidity_to_location_map, humidity)
            locations.append(location)
        # print(pair[0])
        # print(location)

    lowest = min(locations)
    print(f"The lowest location number is {lowest}")
    return lowest
