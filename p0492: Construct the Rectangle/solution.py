"""
# Runtime - 32 ms
# Beats 83.35%

# Memory - 13.9 MB
# Beats 47.43%

# Time Complexity - O(sqrt(n))
# Space Complexity - O(1)
"""

def constructRectangle(area):
    root = int(area ** 0.5)

    while root > 0:
        if area % root == 0:
            return [area // root, root]
        root -= 1
