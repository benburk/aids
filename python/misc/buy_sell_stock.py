"""
Buy Sell Stock

Found in:
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/discuss/39402/Is-this-question-a-joke
"""


def bss_once(prices) -> int:
    """
    Only buy once
    """
    max_profit = 0
    min_price = prices[0]
    for price in prices:
        if price < min_price:
            min_price = price
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit

    return max_profit


def bss_many(prices) -> int:
    """
    Many times
    """
    profit = 0
    for i in range(len(prices) - 1):
        if prices[i + 1] > prices[i]:
            profit += prices[i + 1] - prices[i]
    return profit


def test():
    """run test cases"""
    assert bss_many([7, 1, 5, 3, 6, 4]) == 7
    assert bss_many([1, 2, 3, 4, 5]) == 4
    assert bss_many([7, 6, 4, 3, 1]) == 0

    assert bss_once([7, 1, 5, 3, 6, 4]) == 5
    assert bss_once([7, 6, 4, 3, 1]) == 0


if __name__ == "__main__":
    test()
