"""
# Runtime - 39 ms
# Beats 46.91%

# Memory - 13.8 MB
# Beats 95.57%

# Time Complexity - O(log(n))
# Space Complexity - O(1)
"""

def isPerfectSquare(num):
    if num == 1:
        return True

    l = 1
    r = num // 2

    while l <= r:
        mid = (l + r) // 2

        if mid * mid < num:
            l = mid + 1
            continue

        if mid * mid > num:
            r = mid - 1
            continue

        return True

    return False