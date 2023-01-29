"""
# Runtime - 119 ms
# Beats 65.49%

# Memory - 14.1 MB
# Beats 95.9%

# Time Complexity - O(n)
# Space Complexity - O(n)
"""

def firstUniqChar(s):
    freq = {}

    for x in s:
        freq[x] = freq.get(x, 0) + 1

    for i, x in enumerate(s):
        if freq[x] == 1:
            return i

    return -1