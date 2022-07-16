"""
longest palindrome
"""


def longest_palindrome_naive(string: str):
    """
    naive solution
    O(n^3)
    """
    best = ""
    for length in range(len(string)):  # for each palindrome length
        for j in range(len(string) - length):  # for each starting position
            current = string[j : j + length + 1]
            if len(current) > len(best) and current == current[::-1]:
                best = current
    return best


def golfed(string):
    """one liner"""
    if not string:
        return ""
    return max(
        (
            string[j : j + i + 1]
            for i in range(len(string))
            for j in range(len(string) - i)
            if string[j : j + i + 1] == string[j : j + i + 1][::-1]
        ),
        key=len,
    )


def test():
    """run test cases"""
    test_cases = (
        ("", ""),
        ("a", "a"),
        ("ab", "a"),
        ("aa", "aa"),
        ("aba", "aba"),
        ("cbbd", "bb"),
        ("abbccddccx", "ccddcc"),
    )

    for arg, expected in test_cases:
        assert golfed(arg) == expected
        assert longest_palindrome_naive(arg) == expected


if __name__ == "__main__":
    test()
