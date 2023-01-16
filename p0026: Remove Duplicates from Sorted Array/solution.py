"""
# Runtime - 84 ms
# Beats 96.19%

# Memory - 15.6 MB
# Beats 63.76%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

def removeDuplicates(nums):
    n = len(nums)

    slow = 1

    for fast in range(1, n):
        if nums[fast - 1] != nums[fast]:
            nums[slow] = nums[fast]
            slow += 1

    return slow