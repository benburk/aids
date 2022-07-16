"""knight on keypad

How many distinct numbers can you dial in N hops from a particular
starting position?

https://medium.com/@alexgolec/google-interview-questions-deconstructed-the-knights-dialer-f780d516f029
https://www.reddit.com/r/programming/comments/9mhv8a/google_engineer_breaks_down_the_interview/

Found in:
    https://leetcode.com/problems/knight-dialer/
"""
from functools import lru_cache


def solve(steps):
    """
    recursive with memoization
    """
    neighbours = {
        0: (4, 6),
        1: (6, 8),
        2: (7, 9),
        3: (4, 8),
        4: (0, 3, 9),
        5: (),
        6: (0, 1, 7),
        7: (2, 6),
        8: (1, 3),
        9: (2, 4),
    }

    @lru_cache(None)
    def recursive(current, steps_left):
        if steps_left == 0:
            return 1
        if steps_left == 1:
            return len(neighbours[current])
        total = 0
        for neighbour in neighbours[current]:
            total += recursive(neighbour, steps_left - 1)
        return total

    total = 0
    for i in range(10):
        total += recursive(i, steps - 1)
    return total


def test():
    """run test cases"""
    assert solve(1) == 10
    assert solve(2) == 20
    assert solve(3) == 46


if __name__ == "__main__":
    test()
