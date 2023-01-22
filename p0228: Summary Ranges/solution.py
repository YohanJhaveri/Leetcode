"""
# Runtime - 33 ms
# Beats 71.19%

# Memory - 13.8 MB
# Beats 67.29%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

def summaryRanges(nums):
    ranges = []
    n = len(nums)

    slow = 0
    fast = 1

    while slow < n:
        if fast < n and nums[fast - 1] + 1 == nums[fast]:
            fast += 1
        else:
            ranges.append([nums[slow], nums[fast - 1]])
            slow = fast
            fast = slow + 1

    return [str(x[0]) + "->" + str(x[1]) if x[0] != x[1] else str(x[0]) for x in ranges]