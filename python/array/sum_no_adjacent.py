"""Given a list on non-negative integers, find the max sum without using adjacent
numbers.

Found in:
    https://leetcode.com/problems/house-robber/
"""
from typing import Iterable

import pytest


def max_sum(nums: Iterable[int]) -> int:
    """Find the max sum without using adjacent numbers in a list of positive numbers.

    Observe the next two elements and select the one that maximizes the sum.
    time: O(n)

    :param nums: iterable of positive numbers
    :return: max sum of non-adjacent numbers
    """
    prev1, prev2 = 0, 0
    for num in nums:
        prev1, prev2 = max(prev2 + num, prev1), prev1

    return prev1


@pytest.mark.parametrize(
    "test_input, expected",
    (([], 0), ([1], 1), ([1, 2, 3, 1], 4), ([4, 2, 3, 4], 8), ([2, 7, 9, 3, 1], 12)),
)
def test(test_input: list[int], expected: int) -> None:
    """Run test cases.

    :param test_input: The input to the function.
    :param expected: The expected output.
    """
    assert max_sum(test_input) == expected
