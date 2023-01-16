"""
# Runtime - 24 ms
# Beats 97.79%

# Memory - 13.9 MB
# Beats 11.31%

# Time Complexity - O(n)
# Space Complexity - O(n)
"""

def inorderTraversal(root):
    stack = [(root, False)]
    order = []

    while stack:
        node, seen = stack.pop()

        if seen:
            order.append(node.val)
        elif node:
            stack.append((node.right, False))
            stack.append((node, True))
            stack.append((node.left, False))

    return order