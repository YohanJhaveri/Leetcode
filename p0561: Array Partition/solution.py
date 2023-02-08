"""
# Runtime - 271 ms
# Beats 87.13%

# Memory - 16.7 MB
# Beats 78.19%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

def arrayPairSum(nums):
    nums.sort()
    n = len(nums)
    t = 0

    for i in range(0, n, 2):
        t += nums[i]

    return t