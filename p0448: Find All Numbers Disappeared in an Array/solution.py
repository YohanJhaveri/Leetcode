"""
# Runtime - 386 ms
# Beats 52.72%

# Memory - 21.9 MB
# Beats 89.7%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

def findDisappearedNumbers(nums):
    n = len(nums)
    ans = []

    for x in nums:
        i = abs(x) - 1
        nums[i] = min(nums[i], -nums[i])

    for i, x in enumerate(nums):
        ans += (x > 0) * [i + 1]

    return ans