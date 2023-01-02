"""Generate all permutations of n objects."""
from typing import Iterable

import pytest


def permute2(arr: list[int], n: int) -> Iterable[list[int]]:
    """simpler to understand
    fix element at end
    permute the rest
    """

    if n == 1:
        yield arr
        return
    for i in range(n):
        arr[i], arr[n - 1] = arr[n - 1], arr[i]
        yield from permute2(arr, n - 1)
        arr[i], arr[n - 1] = arr[n - 1], arr[i]


def permute(arr: list[int], n: int) -> Iterable[list[int]]:
    """Computes all permutations of an array using Heap's algorithm.
    time: O(n!)
    """
    if n == 1:
        yield arr
        return

    for i in range(n):
        yield from permute(arr, n - 1)
        if n % 2:
            arr[0], arr[n - 1] = arr[n - 1], arr[0]
        else:
            arr[i], arr[n - 1] = arr[n - 1], arr[i]


@pytest.mark.parametrize(
    "test_input, n, expected",
    ((([], 2, ([],))), (([1], 2, ([1],))), (([1, 2], 2, ([1, 2], [2, 1])))),
)
def test(test_input: list[int], n: int, expected: int) -> None:
    """Run test cases.

    :param test_input: The input to the function.
    :param expected: The expected output.
    """
    # assert tuple(permute(test_input, n)) == expected
    assert tuple(permute2(test_input, n)) == expected


# for p in permute([1, 2, 3, 4], 4):
#     print(p)
# print("")

# for p in permute2([1, 2, 3, 4], 4):
#     print(p)


# print(sorted([str(x) for x in permute([1, 2, 3, 4], 4)]))
