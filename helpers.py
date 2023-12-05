from typing import Tuple, Iterable, Any


def get_lines(input: str):
    lines = input.split('\n')
    for line in lines:
        if not line.strip():
            continue

        yield line


def get_all_lines(input: str):
    lines = input.split('\n')
    return [line for line in lines if line.strip()]


class Grid:
    """
    A simple grid class.

    All coords are in the format (row, column).
    """

    def __init__(self, input: str):
        rows = input.split("\n")
        self.map = [list(row) for row in rows]

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
