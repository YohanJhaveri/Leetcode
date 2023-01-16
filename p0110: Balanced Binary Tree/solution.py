"""
# Runtime - 66 ms
# Beats 55.27%

# Memory - 18.7 MB
# Beats 42.93%

# Time Complexity - O(n)
# Space Complexity - O(n)
"""

def isBalanced(root):
    def maxDepth(node):
        if node:
            L = maxDepth(node.left)
            R = maxDepth(node.right)

            return 1 + max(L, R)

        return 0

    if root:
        return abs(maxDepth(root.left) - maxDepth(root.right)) <= 1 and isBalanced(root.left) and isBalanced(root.right)

    return True