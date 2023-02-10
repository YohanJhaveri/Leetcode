"""
# Runtime - 299 ms
# Beats 89.71%

# Memory - 15.9 MB
# Beats 43.81%

# Time Complexity - O(n)
# Space Complexity - O(n)
"""

def findLHS(nums):
    freq = {}
    maximum = 0

    for x in nums:
        freq[x] = freq.get(x, 0) + 1

    for x in freq:
        if x + 1 in freq:
            maximum = max(maximum, freq[x] + freq[x + 1])

    return maximum