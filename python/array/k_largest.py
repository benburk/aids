"""Returns the k largest elements in an array
"""
import heapq

import pytest


def k_largest_selection(arr: list[int], k: int) -> list[int]:
    """Find k largest elements. Mutates input array.

    Solve by running k iterations of selection sort
    time: O(nk)

    :param arr: list of integers
    :param k: number of largest elements to return
    :return: list of k largest elements
    """
    if k >= len(arr):
        return sorted(arr, reverse=True)
    for i in range(k):
        min_idx = i
        for j in range(i + 1, len(arr)):
            # Select the largest value
            if arr[j] > arr[min_idx]:
                min_idx = j
        # swap the element to the end of the sorted array
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr[:k]


def klarge_maxheap(arr: list[int], k: int) -> list[int]:
    """Find k largest elements.

    Solve by building heap and popping k elements off.
    time: O(n + klogk)
    :param arr: list of integers
    :param k: number of largest elements to return
    :return: list of k largest elements
    """
    return heapq.nlargest(k, arr)


@pytest.mark.parametrize(
    "arr, k, expected",
    (([], 2, []), ([1], 2, [1]), ([1, 2], 2, [2, 1]), ([3, 5, 2, 6, 1, 4], 2, [6, 5])),
)
def test(arr: list[int], k: int, expected: list[int]) -> None:
    """Run test cases.

    :param arr: The input array.
    :param k: The number of largest elements to retrieve.
    :param expected: The k largest elements.
    """
    assert k_largest_selection(arr, k) == expected
