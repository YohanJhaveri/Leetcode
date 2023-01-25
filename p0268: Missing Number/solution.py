"""
# Runtime - 134 ms
# Beats 86.38%

# Memory - 15.2 MB
# Beats 72.97%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

def missingNumber(nums):
    n = len(nums)
    m = 0

    for i in range(n + 1):
        m ^= i

    for x in nums:
        m ^= x

    return m
