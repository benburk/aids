def solve2(arr, target):
    min_len = len(arr) + 1
    curr_sum = 0
    left = 0
    for right, val in enumerate(arr):
        curr_sum += val
        while curr_sum >= target:
            curr_sum -= arr[left]
            min_len = min(right - left + 1, min_len)
            left += 1
    return min_len if min_len != len(arr) + 1 else 0


def max_subarray(arr):
    max_ending_here = max_so_far = arr[0]
    for x in arr[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


def longest_subarray(arr):
    max_ending_here = max_so_far = arr[0]
    start = end = 0
    for i, x in enumerate(arr[1:], 1):
        if max_ending_here < 0:
            start = i
        max_ending_here = max(x, max_ending_here + x)

        if max_ending_here > max_so_far:
            end = i + 1
        max_so_far = max(max_so_far, max_ending_here)
    return end - start


def main():
    test_cases = (
        ((-7, 2, 9, -8, 10), 4),
        ((-7, 2, 9, -8, 10), 4),
        ((-7, 2, 9, -8, 10), 4),
        ((-7, 2, 9, -8, 10), 4),
    )
    for args in test_cases:
        print(f"{args[:-1]} -> {max_subarray(*args[:-1])}, expected: {args[-1]}")


if __name__ == "__main__":
    main()
