"""
# Runtime - 41 ms
# Beats 58.28%

# Memory - 13.8 MB
# Beats 97.43%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

def searchInsert(nums, target):
    n = len(nums)

    l = 0
    r = n - 1

    while l <= r:
        m = (l + r) // 2

        if nums[m] < target:
            l = m + 1
            continue

        if nums[m] > target:
            r = m - 1
            continue

        return m

    return l