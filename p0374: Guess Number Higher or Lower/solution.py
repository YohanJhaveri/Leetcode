"""
# Runtime - 29 ms
# Beats 83.95%

# Memory - 13.8 MB
# Beats 58.6%

# Time Complexity - O(log(n))
# Space Complexity - O(1)
"""

def guessNumber(n):
    l = 1
    r = n

    while l <= r:
        mid = (l + r) // 2

        if guess(mid) == -1:
            r = mid - 1
            continue

        if guess(mid) == 1:
            l = mid + 1
            continue

        return mid