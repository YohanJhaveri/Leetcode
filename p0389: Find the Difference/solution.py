"""
# Runtime - 45 ms
# Beats 40.31%

# Memory - 13.9 MB
# Beats 67.38%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

def findTheDifference(s, t):
    new = 0

    for x in s:
        new ^= ord(x)

    for x in t:
        new ^= ord(x)

    return chr(new)