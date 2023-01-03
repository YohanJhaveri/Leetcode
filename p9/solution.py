"""
# Runtime - 139 ms
# Beats 27.94%

# Memory - 13.9 MB
# Beats 58.55%

# Time Complexity - O(log(n))
# Space Complexity - O(1)
"""

def isPalindrome(x):
    if x < 0:
        return False

    n = 0
    y = 0

    # Finding the number of digits in `x`
    while x // (10 ** n) != 0:
        n += 1

    # Deriving the reverse of `x`
    for i in range(n):
        d = (x // (10 ** i)) % 10
        m = 10 ** (n - i - 1)
        y += d * m

    return x == y