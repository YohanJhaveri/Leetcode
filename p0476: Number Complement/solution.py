"""
# Runtime - 31 ms
# Beats 73.7%

# Memory - 13.9 MB
# Beats 47.62%

# Time Complexity - O(log(n))
# Space Complexity - O(1)
"""

def findComplement(num):
    ans = 0
    idx = 0

    while num:
        ans += (not (num % 2)) * (2 ** idx)
        idx += 1
        num >>= 1

    return ans