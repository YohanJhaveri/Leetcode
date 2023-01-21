"""
# Runtime - 43 ms
# Beats 77.6%

# Memory - 14.1 MB
# Beats 86.15%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

def isIsomorphic(s, t):
    st = {}
    ts = {}

    m = len(s)
    n = len(t)

    if m != n:
        return False

    for i in range(n):
        if s[i] in st and st[s[i]] != t[i]:
            return False
        else:
            st[s[i]] = t[i]

        if t[i] in ts and ts[t[i]] != s[i]:
            return False
        else:
            ts[t[i]] = s[i]

    return True