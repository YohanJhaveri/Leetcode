"""
# Runtime - 769 ms
# Beats 38.38%

# Memory - 13.8 MB
# Beats 94.59%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

def arrangeCoins(n):
    count = 1

    while n >= 0:
        n -= count
        count += 1

    return count - 2