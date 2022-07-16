"""
Reverse a string
"""


def reverse(string) -> str:
    """
    reverse a string
    O(n) space
    O(n) time
    """
    string = list(string)

    for i in range(len(string) // 2):
        string[i], string[-i - 1] = string[-i - 1], string[i]
    return "".join(string)


def test():
    """run test cases"""
    test_cases = (("", ""), ("a", "a"), ("ab", "ba"), ("abcde", "edcba"))
    for arg, expected in test_cases:
        assert reverse(arg) == expected


if __name__ == "__main__":
    test()
