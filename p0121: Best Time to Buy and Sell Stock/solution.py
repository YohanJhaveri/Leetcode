"""
# Runtime - 1055 ms
# Beats 83.63%

# Memory - 25 MB
# Beats 36.47%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

def maxProfit(prices):
    min_price = float("inf")
    max_profit = 0

    for price in prices:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)

    return max_profit