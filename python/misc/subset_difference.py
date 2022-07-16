import functools


def minimum_subset_difference(arr):
    """
    find the minimal difference between any two subsets of arr
    """
    sum_total = sum(arr)

    @functools.lru_cache()
    def solve(i, sum_calc=0):
        # If we have reached last element. Sum of one subset is sumCalculated,
        # sum of other subset is sumTotal-sumCalculated. Return absolute
        # difference of two sums.
        if i == 0:
            return abs((sum_total - sum_calc) - sum_calc)

        # For every item arr[i], we have two choices
        # (1) We do not include it first set
        # (2) We include it in first set
        # We return minimum of two choices
        return min(solve(i - 1, sum_calc + arr[i - 1]), solve(i - 1, sum_calc))

    return solve(len(arr))


def partition_equal_subset(arr):
    """
    can an array be partitioned into 2 subsets such that the difference
    of their sums is 0
    if sum is odd, return false
    subset_sum(arr, sum(arr)//2)
    """
    pass


def main():
    print(minimum_subset_difference([3, 1, 4, 2, 2, 1]))
    print(minimum_subset_difference([1, 5, 11, 5]))


if __name__ == "__main__":
    main()
