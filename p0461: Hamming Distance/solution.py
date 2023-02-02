"""
# Runtime - 36 ms
# Beats 49.85%

# Memory - 13.8 MB
# Beats 95.21%

# Time Complexity - O(log(n))
# Space Complexity - O(1)
"""

def hammingDistance(x, y):
    r = x ^ y
    c = 0

    while r:
        r &= r - 1
        c += 1

    return c