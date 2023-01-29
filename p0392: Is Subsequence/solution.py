"""
# Runtime - 35 ms
# Beats 67.92%

# Memory - 14 MB
# Beats 35.27%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

def isSubsequence(s, t):
    sn = len(s)
    tn = len(t)

    si = 0
    ti = 0

    while si < sn and ti < tn:
        if s[si] == t[ti]:
            si += 1
        ti += 1

    return si == sn