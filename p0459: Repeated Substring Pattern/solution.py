"""
# Runtime - 38 ms
# Beats 83.63%

# Memory - 14.1 MB
# Beats 24.51%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

def repeatedSubstringPattern(s):
    return s in (2 * s)[1:-1]