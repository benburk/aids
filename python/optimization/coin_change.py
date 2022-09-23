"""
You are given coins of different denominations and a total amount of money
amount. Write a function to compute the fewest number of coins that you need
to make up that amount. If that amount of money cannot be made up by any
combination of the coins, return -1.

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1
"""


def count_coin_change_recur(S, m, n):
    """count every way to make change"""

    # If n is 0 then there is 1
    # solution (do not include any coin)
    if n == 0:
        return 1

    # If n is less than 0 then no
    # solution exists
    if n < 0:
        return 0

    # If there are no coins and n
    # is greater than 0, then no
    # solution exist
    if m <= 0 and n >= 1:
        return 0

    # count is sum of solutions (i)
    # including S[m-1] (ii) excluding S[m-1]
    return count_coin_change_recur(S, m - 1, n) + count_coin_change_recur(
        S, m, n - S[m - 1]
    )


def coinChange(self, coins, amount):
    coins.sort(reverse=True)
    lenc, self.res = len(coins), 2**31 - 1

    def dfs(pt, rem, count):
        if not rem:
            self.res = min(self.res, count)
        for i in range(pt, lenc):
            if coins[i] <= rem < coins[i] * (self.res - count):  # if hope still exists
                dfs(i, rem - coins[i], count + 1)

    for i in range(lenc):
        dfs(i, amount, 0)
    return self.res if self.res < 2**31 - 1 else -1


def coin_change(coins: list, amount: int):
    for coin in coins:
        if coin >= amount:
            continue
        tmp = amount // coin
        print(f"{tmp} * ${coin}")
        amount = amount % coin


def main():
    coin_change([5, 2, 1], 11)


if __name__ == "__main__":
    main()
