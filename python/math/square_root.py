"""
Methods for calculating the square root of a number
"""


def newton_sqrt(n):
    """square root using newtons method"""
    x = n
    for _ in range(20):
        x -= (x * x - n) / (2 * x)
    return x


def test():
    """run test cases"""
    print(newton_sqrt(2))


if __name__ == "__main__":
    test()
