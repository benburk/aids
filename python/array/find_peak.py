"""Given an array of integers, find the index of a peak element in it. An array
element is a peak if it is greater than or equal to its neighbors.

Found in:
    https://leetcode.com/problems/find-peak-element/
"""
from typing import Sequence

import pytest


def find_peak(nums: Sequence[int]) -> int:
    """Finds the peak element using a modified binary search.

    time: O(lg(n))
    space: O(1)

    :param nums: array of integers
    :return: index of peak element
    """
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if mid == len(nums) - 1 or nums[mid] > nums[mid + 1]:
            high = mid - 1
        else:
            low = mid + 1
    return low


@pytest.mark.parametrize(
    "test_input, expected",
    (
        ([], 0),
        ([0], 0),
        ([1, 2, 3, 4, 5], 4),
        ([1, 2, 1, 3, 5, 6, 4], 5),
        ([1, 2, 3, 1], 2),
    ),
)
def test(test_input: list[int], expected: int) -> None:
    """Run test cases.

    :param test_input: The input to the function.
    :param expected: The expected output.
    """
    assert find_peak(test_input) == expected
