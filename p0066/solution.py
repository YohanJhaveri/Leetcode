"""
# Runtime - 41 ms
# Beats 58.28%

# Memory - 13.8 MB
# Beats 97.43%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

def plusOne(digits):
    n = len(digits)
    i = n - 1

    while i >= 0:
        if digits[i] == 9:
            digits[i] = 0
            i -= 1
            continue

        else:
            digits[i] += 1
            return digits

    return [1] + digits