def solve(digits: str) -> str:
    if digits == "":
        return []
    lookup = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    from itertools import product

    return ["".join(x) for x in product(*[list(lookup[digit]) for digit in digits])]


def main():
    tests = ("23", "")
    for test in tests:
        print(solve(test))


if __name__ == "__main__":
    main()
