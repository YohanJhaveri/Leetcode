"""
# Runtime - 49 ms
# Beats 36.20%

# Memory - 13.9 MB
# Beats 48.47%

# Time Complexity - O(sqrt(n))
# Space Complexity - O(1)
"""

def checkPerfectNumber(num):
    dsum = 0
    root = ceil(num ** 0.5)

    for i in range(1, root):
        dsum += (num % i == 0) * (i + num // i)

    return 2 * num == dsum