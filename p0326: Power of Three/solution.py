"""
# Runtime - 89 ms
# Beats 78.59%

# Memory - 13.8 MB
# Beats 95.49%

# Time Complexity - O(1)
# Space Complexity - O(1)
"""

def isPowerOfThree(n):
    return n > 0 and (3**19) % n == 0