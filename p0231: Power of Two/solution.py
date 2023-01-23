"""
# Runtime - 30 ms
# Beats 90.27%

# Memory - 13.8 MB
# Beats 94.42%

# Time Complexity - O(1)
# Space Complexity - O(1)
"""

def isPowerOfTwo(n):
    if n == 0:
        return False

    return n & (n - 1) == 0