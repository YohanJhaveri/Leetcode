"""
# Runtime - 787 ms
# Beats 91.29%

# Memory - 16.2 MB
# Beats 72.34%

# Time Complexity - O(1)
# Space Complexity - O(1)
"""

def distributeCandies(candyType):
    return min(len(candyType) // 2, len(set(candyType)))