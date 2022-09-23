import itertools
from typing import Iterable, Iterator, Sequence


def stars_and_bars(n_items: int, n_bins: int) -> Iterator[list[int]]:
    """Generate all permutations for putting n indistinguishable items into k
    distinguishable bins.

    There are n+k-1 choose k-1 ways of partitioning n items into k bins.

    :param n_items: The number of indistinguishable items
    :param n_bins: The number of distinguishable bins
    :return: The permutations of all possibilities.

    Links:
    https://stackoverflow.com/a/28969798/9518712
    """
    for combo in itertools.combinations(range(n_items + n_bins - 1), n_bins - 1):
        yield [
            b - a - 1 for a, b in zip((-1,) + combo, combo + (n_items + n_bins - 1,))
        ]
