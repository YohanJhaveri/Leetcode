"""
# Runtime - 61 ms
# Beats 94.16%

# Memory - 15.2 MB
# Beats 52.45%

# Time Complexity - O(n)
# Space Complexity - O(n)
"""

def twoSum(nums, target):
    indices = {}

    for i1, n1 in enumerate(nums):
        n2 = target - n1
                
        if n2 in indices:
            i2 = indices[n2]
            return [i1, i2]

        indices[n1] = i1