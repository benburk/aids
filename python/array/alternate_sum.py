"""Alternate sum.

Given an array of integers, calculate the alternate sum by alternating between
adding and subtracting the term.

Examples:
[x1, x2, x3] -> x1 - x2 + x3
"""
from typing import Iterable

import pytest


def solve(arr: Iterable[int]) -> int:
    """Calculate the alternate sum of an array of ints.
    time: O(n)
    space: O(1)

    :param arr: The array to sum alternately.
    :return: The alternate sum
    """
    return sum(-x if i % 2 else x for i, x in enumerate(arr))


@pytest.mark.parametrize(
    "test_input, expected",
    (([], 0), ([1], 1), ([5, 2, 1, 3, 4], 5), ([1, 2, 3, 4, 5], 3)),
)
def test(test_input: list[int], expected: int) -> None:
    """Run test cases."""
    assert solve(test_input) == expected
