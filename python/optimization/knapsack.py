"""
The decision problem form of the knapsack problem (Can a value of at least V
be achieved without exceeding the weight W?) is NP-complete, thus there is no
known algorithm both correct and fast (polynomial-time) in all cases.
"""


def knapsack_one(weights, values, capacity):
    """knapsack 0-1 problem"""

    def solve(cap, n):
        if n == 0 or cap == 0:
            return 0

        # if adding the nth item puts knapsack over capacity, skip it
        if weights[n - 1] > cap:
            return solve(cap, n - 1)

        # return the maximum of two cases:
        # (1) nth item included
        # (2) not included
        return max(
            values[n - 1] + solve(cap - weights[n - 1], n - 1), solve(cap, n - 1)
        )

    def solve2(cap, i=0):
        if cap < 0:
            return -sum(values), []
        if i == len(weights):
            return 0, []
        res1 = solve2(cap, i + 1)
        res2 = solve2(cap - weights[i], i + 1)
        res2 = (res2[0] + values[i], [i] + res2[1])
        return max(res1, res2)

    return solve(capacity, len(values))


def main():
    items = [(4, 12), (2, 1), (6, 4), (1, 1), (2, 2)]
    weight, size = zip(*items)
    weight = list(weight)
    size = list(size)
    capacity = 15
    print(knapsack_one(size, weight, capacity))


if __name__ == "__main__":
    main()
