"""
Binary search

References:
- https://en.wikipedia.org/wiki/Binary_search_algorithm
"""
from typing import Optional, Sequence

import pytest


def binary_search(arr: Sequence[int], target: int) -> Optional[int]:
    """
    arr must be sorted, O(nlogn)
    given an array and a target value, return the index
    returns -1 if the target is not present

    Best case: O(1)
    Worst case: O(log n)
    Worst case space: O(1)
    """
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return mid
    return None

    # replace with this line for nearest
    # return low if arr[low] - target < target - arr[high] else high


def binary_search_recur(
    arr: Sequence[int], low: int, high: int, num: int
) -> Optional[int]:
    """
    recursive variant of binary search
    """
    if low > high:  # error case
        return None
    mid = (low + high) // 2
    if num < arr[mid]:
        return binary_search_recur(arr, low, mid - 1, num)
    if num > arr[mid]:
        return binary_search_recur(arr, mid + 1, high, num)
    return mid


@pytest.mark.parametrize(
    "arr, target, expected",
    (
        ([1, 2, 4, 7, 9, 11], 5, None),
        ([3, 5, 7, 8, 9, 10], 3, 0),
        ([1, 5, 8, 10], 0, None),
        ([1, 5, 8, 10], 5, 1),
    ),
)
def test(arr: list[int], target: int, expected: int) -> None:
    """run test cases"""
    assert binary_search(arr, target) == expected


if __name__ == "__main__":
    test()
