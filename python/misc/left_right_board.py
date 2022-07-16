"""
given two arrays consisting of 1s, 0s, and -1s
1s can only move right
-1s can only move left
they cannot jump over each other
decide whether an end configuration can be obtained from a start configuration
"""


def solve(initial: list, final: list) -> bool:
    """O(n) time complexity, O(1) space
    condition: len(initial) == len(final) >= 0"""
    i = j = 0
    while i < len(initial) or j < len(final):
        while i < len(initial) and initial[i] == 0 and (i < j or final[j] == -1):
            i += 1
        while j < len(final) and final[j] == 0 and (j < i or initial[i] == 1):
            j += 1
        if i < len(initial) and j < len(final) and initial[i] != final[j]:
            return False
        i += 1
        j += 1
    return i == j


def solve2(initial: list, final: list) -> bool:
    assert len(initial) == len(final)
    i = j = 0

    while i < len(initial) and j < len(final):
        if initial[i] == final[j]:
            i += 1
            j += 1
            while i < j and initial[i] == 0:
                i += 1
            while j < i and final[j] == 0:
                j += 1
        elif initial[i] == 1 and final[j] == 0:
            j += 1
        elif final[j] == -1 and initial[i] == 0:
            i += 1
        else:
            return False
    return i == j


def main():
    """test our function"""
    test_cases = (
        ([], [], True),
        ([1], [1], True),
        ([1, -1], [-1, 1], False),
        ([1, 0, -1], [0, 1, -1], True),
        ([1, 0, 1], [1, 1, 0], False),
        ([1, 0, 0, 1, -1], [0, 1, 0, 1, -1], True),
        ([1, 0, 0, 1, -1], [0, 1, 1, 1, -1], False),
        ([1, 0, 0, 1], [0, 1, 1, 0], False),
        ([1, 0, 1, -1, 0, -1], [0, 1, 1, -1, -1, -1], False),
        ([1, 0, 1, -1, 0, -1], [0, 1, 1, -1, -1, 0], True),
        ([1, 0, 1, 1, -1, -1, 0, -1], [1, 1, 0, 1, -1, 0, -1, -1], False),
        ([1, 0, 1, 1, -1], [0, 1, 0, 1, -1], False),
        ([1, 1, 0, 1, -1, 0, -1, -1], [1, 0, 1, 1, -1, -1, 0, -1], True),
        ([1, 1, 0, 1, -1, 1, -1, -1], [1, 0, 1, 1, -1, -1, 0, -1], False),
        ([-1, 0, 0, 0, 0, -1, 1, 1, 0], [-1, -1, 0, 0, 0, 0, 0, 1, 1], True),
        ([1, -1, 0, 1, 0], [-1, 1, 0, 0, 1], False),
        ([0, 1, -1, 0, 1, 0], [-1, 0, 1, 0, 0, 1], False),
        ([0, 1, 1, 0, -1, 0], [0, 1, 0, 1, -1, 0], True),
    )
    for args in test_cases:
        print(f"{args[:-1]} -> {solve(*args[:-1])}, expected: {args[-1]}")


if __name__ == "__main__":
    main()
