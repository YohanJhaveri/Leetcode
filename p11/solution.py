"""
# Runtime - 755 ms
# Beats 91.13%

# Memory - 27.5 MB
# Beats 46.60%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

def maxArea(height):
    n = len(height)

    i = 0
    j = n - 1

    most = 0

    while i < j:
        area = min(height[j], height[i]) * (j - i)
        most = max(area, most)

        if height[i] < height[j]:
            i += 1
        else:
            j -= 1

    return most