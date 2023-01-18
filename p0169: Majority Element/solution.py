"""
# Runtime - 26 ms
# Beats 94.25%

# Memory - 13.9 MB
# Beats 54.80%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

def majorityElement(nums):
    major = nums[0]
    count = 0

    for n in nums:
        if n == major:
            count += 1
        else:
            count -= 1

        if count < 0:
            major = n
            count = 0

    return major