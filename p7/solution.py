"""
# Runtime - 29 ms
# Beats 96.14%

# Memory - 13.9 MB
# Beats 64.17%

# Time Complexity - O(log(n))
# Space Complexity - O(1)
"""

def reverse(x):
    MIN_INTEGER = -(2 ** 31)
    MAX_INTEGER = (2 ** 31) - 1

    is_negative = x < 0

    x = abs(x)
    y = 0
    n = 0

    # Finding the number of digits in `x`
    while (x // (10 ** n)) != 0:
        n += 1

    # Deriving the reverse of `x`
    while x:
        y += (x % 10) * (10 ** (n - 1))
        x //= 10
        n -= 1

    if MIN_INTEGER <= y <= MAX_INTEGER:
        return y * (-1 if is_negative else 1)

    return 0