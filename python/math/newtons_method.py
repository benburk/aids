"""
Newton's method
"""


def newtons(func, f_prime, guess, epsilon=0.0001):
    """newtons method
    Args:
        func (callable): the function to find roots for
        f_prime (callable): the derivative of func
        guess: the initial guess
    """
    while abs(func(guess)) > epsilon:  # close to zero?
        guess -= func(guess) / f_prime(guess)
    return guess


def test():
    """run test cases"""
    # print(newtons(f, df, -5, 1e-5))


if __name__ == "__main__":
    test()
