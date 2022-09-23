import itertools
from typing import Iterable, Sequence


def powerset(arr: Sequence[int], k: int) -> Iterable[tuple[int, ...]]:
    """Compute the powerset of a list
    time: O(2^n)
    """
    yield from itertools.chain.from_iterable(
        itertools.combinations(arr, i) for i in range(1, len(arr) + 1)
    )
