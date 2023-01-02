import itertools
from typing import Iterable, Sequence

import pytest


def powerset(arr: Sequence[int]) -> Iterable[tuple[int, ...]]:
    """Computes the powerset of a list, excluding the empty set.
    time: O(2^n)
    """
    yield from itertools.chain.from_iterable(
        itertools.combinations(arr, i) for i in range(1, len(arr) + 1)
    )


@pytest.mark.parametrize(
    "test_input, expected",
    (([], tuple()), ([1], ((1,),)), ([1, 2], ((1,), (2,), (1, 2)))),
)
def test(test_input: list[int], expected: int) -> None:
    """Run test cases.

    :param test_input: The input to the function.
    :param expected: The expected output.
    """
    assert tuple(powerset(test_input)) == expected
