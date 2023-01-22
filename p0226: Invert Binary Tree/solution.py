"""
# Runtime - 42 ms
# Beats 47.43%

# Memory - 13.8 MB
# Beats 53.60%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

def invertTree(root):
    if root:
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

    return root