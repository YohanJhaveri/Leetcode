"""
# Runtime - 39 ms
# Beats 54.83%

# Memory - 13.8 MB
# Beats 94.76%

# Time Complexity - O(1)
# Space Complexity - O(1)
"""

def addDigits(num):
    if num == 0:
        return 0

    return num % 9 or 9