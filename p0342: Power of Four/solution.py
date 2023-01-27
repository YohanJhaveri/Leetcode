"""
# Runtime - 31 ms
# Beats 86.74%

# Memory - 13.8 MB
# Beats 47.19%

# Time Complexity - O(1)
# Space Complexity - O(1)
"""

def isPowerOfFour(n):
    return n > 0 and n & (n-1) == 0 and 0b1010101010101010101010101010101 & n == n