"""
# Runtime - 48 ms
# Beats 82.47%

# Memory - 14.5 MB
# Beats 63.22%

# Time Complexity - O(n)
# Space Complexity - O(n)
"""

def isAnagram(s, t):
    cache = {}

    for x in s:
        cache[x] = cache.setdefault(x, 0) + 1

    for x in t:
        cache[x] = cache.setdefault(x, 0) - 1

        if cache[x] < 0:
            return False

    return sum([cache[x] for x in cache]) == 0