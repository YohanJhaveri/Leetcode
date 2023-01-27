"""
# Runtime - 213 ms
# Beats 51.38%

# Memory - 18.4 MB
# Beats 81.38%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

def reverseString(s):
    l = 0
    r = len(s) - 1

    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1