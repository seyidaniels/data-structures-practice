import sys


def maxProfit(prices):
    if len(prices) == 0 or len(prices) == 1:
        return 0
    maxProfit = 0
    maxPrice = sys.maxsize

    i = 0
    while i < len(prices):
        if prices[i] < maxPrice:
            maxPrice = prices[i]
        elif prices[i] - maxPrice > maxProfit:
            maxProfit = prices[i] - maxPrice
        i += 1
    return maxProfit


p = maxProfit([1, 2, 3, 4, 5])
