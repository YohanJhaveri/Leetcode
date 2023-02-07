"""
# Runtime - 42 ms
# Beats 89.43%

# Memory - 16.3 MB
# Beats 77.92%

# Time Complexity - O(n)
# Space Complexity - O(n)
"""

def diameterOfBinaryTree(root):
    maximum = [0]

    def maxDepth(node):
        if not node:
            return 0

        L = maxDepth(node.left)
        R = maxDepth(node.right)

        maximum[0] = max(maximum[0], L + R)

        return 1 + max(L, R)

    maxDepth(root)

    return maximum[0]