"""
# Runtime - 46 ms
# Beats 79.58%

# Memory - 16 MB
# Beats 44.65%

# Time Complexity - O(n)
# Space Complexity - O(n)
"""

def maxDepth(root):
    if not root:
        return 0

    if not root.children:
        return 1

    depths = []

    for child in root.children:
        depths.append(self.maxDepth(child))

    return 1 + max(depths)