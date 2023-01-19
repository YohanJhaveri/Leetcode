"""
# Runtime - 26 ms
# Beats 94.25%

# Memory - 13.9 MB
# Beats 54.80%

# Time Complexity - O(log(n))
# Space Complexity - O(1)
"""

def titleToNumber(columnTitle):
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    result = 0

    for i, x in enumerate(columnTitle[::-1]):
        result += (letters.index(x) + 1) * 26**i

    return result