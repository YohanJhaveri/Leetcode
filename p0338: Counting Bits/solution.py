"""
# Runtime - 88 ms
# Beats 76.95%

# Memory - 20.8 MB
# Beats 24.39%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

def countBits(n):
    ans = [0] * (n + 1)

    for i in range(1, n + 1):
        ans[i] = ans[i & (i - 1)] + 1

    return ans