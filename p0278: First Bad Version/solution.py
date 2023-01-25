"""
# Runtime - 25 ms
# Beats 94.63%

# Memory - 13.9 MB
# Beats 9.74%

# Time Complexity - O(log(n))
# Space Complexity - O(1)
"""

def firstBadVersion(n):
    i = 1
    j = n

    while i <= j:
        mid = (i + j) // 2

        if isBadVersion(mid):
            if not isBadVersion(mid - 1):
                return mid

            j = mid - 1

        else:
            i = mid + 1