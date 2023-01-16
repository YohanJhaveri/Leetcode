"""
# Runtime - 36 ms
# Beats 81.87%

# Memory - 13.8 MB
# Beats 97.30%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

def removeElement(nums):
    i = 0

    for x in nums:
        if x != val:
            nums[i] = x
            i += 1

    return i