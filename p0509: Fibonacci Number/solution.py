"""
# Runtime - 31 ms
# Beats 79.48%

# Memory - 13.8 MB
# Beats 45.62%

# Time Complexity - O(n)
# Space Complexity - O(n)
"""

def fib(n):
    if n == 0:
        return 0

    seq = [0, 1]

    for i in range(1, n):
        seq.append(seq[-1] + seq[-2])

    return seq[-1]
