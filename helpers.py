from typing import Tuple, Iterable, Any, Union, List


def get_lines(input: str, ignore_newlines: bool = True):
    lines = input.split('\n')
    for line in lines:
        if ignore_newlines:
            if not line.strip():
                continue

        yield line


def get_all_lines(input: str):
    lines = input.split('\n')
    return [line for line in lines if line.strip()]

def get_blank_separated_groups(input: str) -> List[List[str]]:
    groups = []
    group = []
    lines = get_lines(input, ignore_newlines=False)
    for line in lines:
        if not line.strip():
            groups.append(group)
            group = []
        else:
            group.append(line)

    groups.append(group)

    return groups

def multi_iterate(l: List):
    for i in range(0, len(l)):
        if i + 1 == len(l):
            yield l[i], None, i
        else:
            yield l[i], l[i + 1], i

class Grid:
    """
    A simple grid class.

    All coords are in the format (row, column).
    """

    def __init__(self, input: str):
        rows = input.split("\n")
        self.map = [list(row) for row in rows]

    def pretty_print(self) -> None:
        for row in range(len(self.map)):
            print("".join(self.map[row]))

    def all_coords(self) -> Iterable[Tuple[int, int]]:
        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                yield row, col

    def get_coord_value(self, coord: Tuple[int, int]) -> Any:
        return self.map[coord[0]][coord[1]]

    def get_surrounding_coords_span(self, row: int, span: Tuple[int, int]) -> Iterable[Tuple[int, int]]:
        for col in range(span[0], span[1]):
            current = (row, col)
            if col == span[0]:
                yield self.get_bottom_left_coord(current)
                yield self.get_left_coord(current)
                yield self.get_top_left_coord(current)

            yield self.get_top_coord(current)
            yield self.get_bottom_coord(current)

            if col == span[1] - 1:
                yield self.get_bottom_right_coord(current)
                yield self.get_right_coord(current)
                yield self.get_top_right_coord(current)

    def get_adjacent_coords(self, coord: Tuple[int, int], incl_diagonals = False) -> Tuple[
        Union[int, None], ...
    ]:
        """Return a tuple of (left, top, right, bottom) values to coordinate. If adjacent coord does not exist,
        None will be included instead."""
        left = self.get_left_coord(coord)
        top = self.get_top_coord(coord)
        right = self.get_right_coord(coord)
        bottom = self.get_bottom_coord(coord)

        if not incl_diagonals:
            return left, top, right, bottom

        top_left = self.get_top_left_coord(coord)
        top_right = self.get_top_right_coord(coord)
        bottom_left = self.get_bottom_left_coord(coord)
        bottom_right = self.get_bottom_right_coord(coord)

        return left, top_left, top, top_right, right, bottom_right, bottom, bottom_left

    def get_top_coord(self, coord: Tuple[int, int]) -> Any:
        row, col = coord[0], coord[1]
        if row == 0:
            return None

        return row - 1, col

    def get_bottom_coord(self, coord: Tuple[int, int]) -> Any:
        row, col = coord[0], coord[1]
        if row == len(self.map) - 1:
            return None

        return row + 1, col

    def get_left_coord(self, coord: Tuple[int, int]) -> Any:
        row, col = coord[0], coord[1]
        if col == 0:
            return None

        return row, col - 1

    def get_right_coord(self, coord: Tuple[int, int]) -> Any:
        row, col = coord[0], coord[1]
        if col == len(self.map[0]) - 1:
            return None

        return row, col + 1

    def get_top_left_coord(self, coord: Tuple[int, int]) -> Any:
        row, col = coord[0], coord[1]
        if row == 0:
            return None

        if col == 0:
            return None

        return row - 1, col - 1

    def get_bottom_left_coord(self, coord: Tuple[int, int]) -> Any:
        row, col = coord[0], coord[1]
        if row == len(self.map) - 1:
            return None

        if col == 0:
            return None

        return row + 1, col - 1

    def get_top_right_coord(self, coord: Tuple[int, int]) -> Any:
        row, col = coord[0], coord[1]
        if row == 0:
            return None

        if col == len(self.map[0]) - 1:
            return None

        return row - 1, col + 1

    def get_bottom_right_coord(self, coord: Tuple[int, int]) -> Any:
        row, col = coord[0], coord[1]
        if row == len(self.map) - 1:
            return None

        if col == len(self.map[0]) - 1:
            return None

        return row + 1, col + 1

    def get_surrounding_values_span(self, row: int, span: Tuple[int, int]) -> Iterable[Any]:
        for col in range(span[0], span[1]):
            current = (row, col)
            if col == span[0]:
                yield self.get_bottom_left_value(current)
                yield self.get_left_value(current)
                yield self.get_top_left_value(current)

            yield self.get_top_value(current)
            yield self.get_bottom_value(current)

            if col == span[1] - 1:
                yield self.get_bottom_right_value(current)
                yield self.get_right_value(current)
                yield self.get_top_right_value(current)

    def get_adjacent_values(self, coord: Tuple[int, int], incl_diagonals = False) -> Tuple[
        Union[int, None], ...
    ]:
        """Return a tuple of (left, top, right, bottom) values to coordinate. If adjacent coord does not exist,
        None will be included instead."""
        left = self.get_left_value(coord)
        top = self.get_top_value(coord)
        right = self.get_right_value(coord)
        bottom = self.get_bottom_value(coord)

        if not incl_diagonals:
            return left, top, right, bottom

        top_left = self.get_top_left_value(coord)
        top_right = self.get_top_right_value(coord)
        bottom_left = self.get_bottom_left_value(coord)
        bottom_right = self.get_bottom_right_value(coord)

        return left, top_left, top, top_right, right, bottom_right, bottom, bottom_left

    def get_top_value(self, coord: Tuple[int, int]) -> Any:
        row, col = coord[0], coord[1]
        if row == 0:
            return None

        return self.map[row - 1][col]

    def get_bottom_value(self, coord: Tuple[int, int]) -> Any:
        row, col = coord[0], coord[1]
        if row == len(self.map) - 1:
            return None

        return self.map[row + 1][col]

    def get_left_value(self, coord: Tuple[int, int]) -> Any:
        row, col = coord[0], coord[1]
        if col == 0:
            return None

        return self.map[row][col - 1]

    def get_right_value(self, coord: Tuple[int, int]) -> Any:
        row, col = coord[0], coord[1]
        if col == len(self.map[0]) - 1:
            return None

        return self.map[row][col + 1]

    def get_top_left_value(self, coord: Tuple[int, int]) -> Any:
        row, col = coord[0], coord[1]
        if row == 0:
            return None

        if col == 0:
            return None

        return self.map[row - 1][col - 1]

    def get_bottom_left_value(self, coord: Tuple[int, int]) -> Any:
        row, col = coord[0], coord[1]
        if row == len(self.map) - 1:
            return None

        if col == 0:
            return None

        return self.map[row + 1][col - 1]

    def get_top_right_value(self, coord: Tuple[int, int]) -> Any:
        row, col = coord[0], coord[1]
        if row == 0:
            return None

        if col == len(self.map[0]) - 1:
            return None

        return self.map[row - 1][col + 1]

    def get_bottom_right_value(self, coord: Tuple[int, int]) -> Any:
        row, col = coord[0], coord[1]
        if row == len(self.map) - 1:
            return None

        if col == len(self.map[0]) - 1:
            return None

        return self.map[row + 1][col + 1]

    def update_coord_value(self, coord: Tuple[int, int], new_value: Any) -> None:
        self.map[coord[0]][coord[1]] = new_value