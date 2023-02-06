"""
# Runtime - 46 ms
# Beats 27.51%

# Memory - 14 MB
# Beats 87.56%

# Time Complexity - O(n)
# Space Complexity - O(n)
"""

def reverseStr(s, k):
    x = 0
    n = len(s)
    a = list(s)

    while x < n:
        l = x
        r = min(x + k, n) - 1

        while l < r:
            a[l], a[r] = a[r], a[l]
            l += 1
            r -= 1

        x += k * 2

    return "".join(a)