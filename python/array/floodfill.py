"""Flood fill."""
from typing import TypeVar

T = TypeVar("T")


def floodfill(matrix: list[list[T]], i: int, j: int, before: T, after: T) -> None:
    """Flood fill a matrix in-place.

    time: O(n^2)

    :param matrix: 2d list
    :param i: x coord of starting position
    :param j: y coord of starting position
    :param before: the numbers to replace
    :param after: the number to replace with
    """
    if matrix[i][j] == before:
        matrix[i][j] = after
        if i > 0:
            floodfill(matrix, i - 1, j, before, after)
        if i < len(matrix[j]) - 1:
            floodfill(matrix, i + 1, j, before, after)
        if j > 0:
            floodfill(matrix, i, j - 1, before, after)
        if j < len(matrix) - 1:
            floodfill(matrix, i, j + 1, before, after)


def test() -> None:
    """Runs test cases."""
    matrix = [
        [0, 2, 0, 2, 2, 2],
        [0, 0, 0, 0, 0, 0],
        [0, 2, 2, 0, 2, 2],
        [2, 0, 2, 0, 0, 2],
        [0, 2, 0, 0, 2, 0],
        [0, 0, 2, 0, 0, 0],
    ]

    floodfill(matrix, 4, 2, 0, 1)
    assert matrix[1][5] == 1
