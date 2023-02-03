"""
# Runtime - 337 ms
# Beats 92.32%

# Memory - 14.3 MB
# Beats 26.9%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

def findMaxConsecutiveOnes(nums):
    curCount = 0
    maxCount = 0

    for x in nums:
        if x == 0:
            maxCount = max(maxCount, curCount)
            curCount = 0
        else:
            curCount += 1

    return max(maxCount, curCount)