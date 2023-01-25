"""
# Runtime - 166 ms
# Beats 89.7%

# Memory - 15.5 MB
# Beats 57.95%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

def moveZeroes(nums):
    n = len(nums)
    slow = 0

    for fast in range(n):
        if nums[slow] == 0 and nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]

        if nums[slow] != 0:
            slow += 1