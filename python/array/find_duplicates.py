"""Different methods for finding duplicates in an array."""
from typing import Iterable, MutableSequence, Optional, TypeVar

import pytest

T = TypeVar("T")


def solve_bounded(nums: MutableSequence[int]) -> Optional[int]:
    """Finds the first duplicate element if elements are bounded.

    The idea is to use the sign of the element at a position as a flag.
    contraints: 1 <= element <= len(nums)
    time: O(n)
    space: O(1)

    :param nums: The input array
    :return: The first duplicate element, or None if no duplicates
    """
    assert all(x in range(1, len(nums) + 1) for x in nums)
    for num in (abs(x) for x in nums):
        if nums[num - 1] < 0:
            return num
        nums[num - 1] *= -1
    return None


def solve_set(nums: Iterable[T]) -> Optional[T]:
    """Find first duplicate element using a set.

    time: O(n)
    space: O(n)

    :param nums: An iterable of input values
    :return: The first duplicate element, or None if no duplicates
    """
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return None


@pytest.mark.parametrize(
    "test_input, expected", (([], None), ([1], None), ([1, 1], 1), ([2, 1, 3, 2, 3], 2))
)
def test(test_input: list[int], expected: Optional[int]) -> None:
    """Run test cases.

    :param test_input: The input to the function.
    :param expected: The expected output.
    """
    assert solve_set(test_input) == expected
    assert solve_bounded(test_input) == expected
