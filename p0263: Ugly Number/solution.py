"""
# Runtime - 23 ms
# Beats 98.95%

# Memory - 13.8 MB
# Beats 95.5%

# Time Complexity - O(log(n))
# Space Complexity - O(1)
"""

def isUgly(n):
    if n == 0:
        return False

    for x in [5, 3, 2]:
        while n % x == 0:
            n //= x

    return n == 1