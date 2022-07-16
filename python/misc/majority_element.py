"""
Find the majority element, i.e. an element that occurs more than n/2 times
It may not exist
"""


def majority(arr: list):
    """moore's voting algorithm"""
    count = 0
    for val in arr:
        if count == 0:
            major = val
        count += 1 if val == major else -1
    return major if arr.count(major) > len(arr) // 2 else -1


def main():
    test_cases = (
        ([2, 1, 2, 3, 4, 2, 1, 2, 2], 2),
        ([3, 3, 4, 2, 4, 4, 2, 4, 4], 4),
        ([3, 3, 4, 2, 4, 4, 2, 4], -1),
    )
    for args in test_cases:
        print(f"{args[:-1]} -> {majority(*args[:-1])}, expected: {args[-1]}")


if __name__ == "__main__":
    main()
