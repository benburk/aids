"""Generate a random permutation of a finite sequence."""
import random
from typing import MutableSequence


def shuffle_std(arr: MutableSequence[int]) -> None:
    """Shuffle an array using the standard library in-place"""
    random.shuffle(arr)


def shuffle_fy(arr: MutableSequence[int]) -> MutableSequence[int]:
    """Shuffles an array in-place using Fisher-Yates algorithm.

    Space: O(1)
    Links:
        https://en.wikipedia.org/wiki/Fisher–Yates_shuffle
    """
    for i, elem in enumerate(arr):
        rand_idx = random.randrange(i, len(arr))
        arr[i], arr[rand_idx] = arr[rand_idx], elem
    return arr
