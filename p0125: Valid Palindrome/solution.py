"""
# Runtime - 42 ms
# Beats 92.53%

# Memory - 14.6 MB
# Beats 60.85%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

def isPalindrome(s):
    l = 0
    r = len(s) - 1
    s = s.lower()

    alphanumeric = set("abcdefghijklmnopqrstuvwxyz0123456789")

    while l < r:
        L = s[l]
        R = s[r]

        if L not in alphanumeric:
            l += 1
            continue

        if R not in alphanumeric:
            r -= 1
            continue

        if L != R:
            return False

        l += 1
        r -= 1

    return True