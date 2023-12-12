# Day 11 AoC 2023
# f"https://adventofcode.com/2023/day/11"
import helpers
from pprint import pprint

PROBLEM_1_EXAMPLE_1_INPUT = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""
PROBLEM_1_EXAMPLE__1_ANSWER = 374


class GalaxyGrid(helpers.Grid):
    def __init__(self, input: str, expansion_factor: int = 1):
        super().__init__(input)
        self.galaxy_coords = []
        self.expansion_factor = expansion_factor
        if self.expansion_factor > 1:
            self.expansion_factor -= 1

        self._find_initial_coords()
        self._expand_grid()

    def _find_initial_coords(self):
        for row_idx, row in enumerate(self.map):
            for col_idx, col_value in enumerate(row):
                if col_value == "#":
                    self.galaxy_coords.append((row_idx, col_idx))

    def _expand_grid(self):
        expansion_rows = []
        for row_idx, row in enumerate(self.map):
            if "#" not in row:
                expansion_rows.append(row_idx)

        expansion_cols = []
        for col_idx, _ in enumerate(self.map[0]):
            col_empty = True
            for row_idx, row in enumerate(self.map):
                if "#" in row[col_idx]:
                    col_empty = False
                    break

            if col_empty:
                expansion_cols.append(col_idx)

        updated_coords = []
        for coord in self.galaxy_coords:
            row_offset = len([idx for idx in expansion_rows if idx < coord[0]])
            col_offset = len([idx for idx in expansion_cols if idx < coord[1]])
            if self.expansion_factor > 1:
                row_offset *= self.expansion_factor
                col_offset *= self.expansion_factor
            updated_coords.append((coord[0] + row_offset, coord[1] + col_offset))

        self.galaxy_coords = updated_coords

    @staticmethod
    def manhattan_distance(coord_a: tuple[int, int], coord_b: tuple[int, int]) -> int:
        horiz_steps = abs(coord_a[1] - coord_b[1])
        vert_steps = abs(coord_a[0] - coord_b[0])
        return horiz_steps + vert_steps


def sum_smallest_paths(grid: GalaxyGrid) -> int:
    calculated = set()
    sum = 0

    for coord_a in grid.galaxy_coords:
        for coord_b in grid.galaxy_coords:
            if coord_a == coord_b:
                continue

            if f"{coord_a}|{coord_b}" in calculated:
                continue

            sum += grid.manhattan_distance(coord_a, coord_b)
            calculated.add(f"{coord_a}|{coord_b}")
            calculated.add(f"{coord_b}|{coord_a}")

    return sum


def solve_problem_1(input: str):
    grid = GalaxyGrid(input)

    result = sum_smallest_paths(grid)

    print(f"The sum of all shortest paths between pairs is {result}")
    return result


PROBLEM_2_EXAMPLE_1_INPUT = PROBLEM_1_EXAMPLE_1_INPUT
PROBLEM_2_EXAMPLE__1_ANSWER = 8410


def solve_problem_2(input: str, expansion_factor: int = 100):
    grid = GalaxyGrid(input, expansion_factor=expansion_factor)

    result = sum_smallest_paths(grid)

    print(f"The sum of all shortest paths between pairs is {result}")
    return result
