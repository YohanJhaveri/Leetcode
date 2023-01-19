"""
# Runtime - 36 ms
# Beats 67.73%

# Memory - 13.9 MB
# Beats 47.8%

# Time Complexity - O(log(n))
# Space Complexity - O(1)
"""

def hammingWeight(n):
    count = 0

    while n:
        count += n & 1
        n //= 2

    return count