"""
# Runtime - 165 ms
# Beats 84.34%

# Memory - 15.8 MB
# Beats 36.85%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

def findContentChildren(g, s):
    g.sort()
    s.sort()

    i = 0
    j = 0

    for j in range(len(s)):
        if i >= len(g):
            break

        if g[i] <= s[j]:
            i += 1

    return i