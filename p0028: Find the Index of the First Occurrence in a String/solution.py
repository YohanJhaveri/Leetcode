"""
# Runtime - 41 ms
# Beats 58.28%

# Memory - 13.8 MB
# Beats 97.43%

# Time Complexity - O(m * n)
# Space Complexity - O(1)
"""

def strStr(haystack, needle):
    m = len(haystack)
    n = len(needle)

    for s in range(m):
        i = s
        j = 0

        while i < m and j < n and haystack[i] == needle[j]:
            i += 1
            j += 1

        if j == n:
            return s

    return -1