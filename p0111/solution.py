"""
# Runtime - 706 ms
# Beats 49.60%

# Memory - 55 MB
# Beats 22.89%

# Time Complexity - O(n)
# Space Complexity - O(n)
"""

def minDepth(root):
    if not root:
        return 0

    if root and not root.left and not root.right:
        return 1

    if root:
        L = minDepth(root.left) if root.left else float("inf")
        R = minDepth(root.right) if root.right else float("inf")

        return 1 + min(L, R)
