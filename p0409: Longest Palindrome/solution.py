"""
# Runtime - 34 ms
# Beats 75.78%

# Memory - 13.9 MB
# Beats 16.91%

# Time Complexity - O(n)
# Space Complexity - O(n)
"""

def longestPalindrome(s):
    freq = {}
    isOneAdded = False
    total = 0

    for x in s:
        freq[x] = freq.get(x, 0) + 1

    for x in freq:
        total += freq[x] // 2
        isOneAdded = isOneAdded or freq[x] % 2

    return total * 2 + isOneAdded