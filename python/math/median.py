"""
Median in linear time
"""
import random


def quickselect_median(arr):
    """quickselect median"""
    if len(arr) % 2 == 1:
        return quickselect(arr, len(arr) // 2)

    return 0.5 * (quickselect(arr, len(arr) // 2 - 1) + quickselect(arr, len(arr) // 2))


def quickselect(l, k):
    """
    Select the kth element in l (0 based)
    :param l: List of numerics
    :param k: Index
    :param pivot_fn: Function to choose a pivot, defaults to random.choice
    :return: The kth element of l
    """
    if len(l) == 1:
        assert k == 0
        return l[0]

    pivot = random.choice(l)

    lows = [el for el in l if el < pivot]
    highs = [el for el in l if el > pivot]
    pivots = [el for el in l if el == pivot]

    if k < len(lows):
        return quickselect(lows, k)

    if k < len(lows) + len(pivots):
        # We got lucky and guessed the median
        return pivots[0]

    return quickselect(highs, k - len(lows) - len(pivots))


def test():
    """run test cases"""
    arr = [1, 3, 2, 7, 5, 4, 6, 8]
    print(quickselect_median(arr))


if __name__ == "__main__":
    test()
