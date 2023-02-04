"""
# Runtime - 34 ms
# Beats 54.54%

# Memory - 13.8 MB
# Beats 60.7%

# Time Complexity - O(log(n))
# Space Complexity - O(1)
"""

def convertToBase7(num):
    sym = list("01234567")
    neg = num < 0
    num = abs(num)
    ans = ""

    if num == 0:
        return "0"

    while num > 0:
        ans = sym[num % 7] + ans
        num //= 7

    return neg * "-" + ans