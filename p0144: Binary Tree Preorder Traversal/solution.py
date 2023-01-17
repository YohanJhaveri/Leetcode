"""
# Runtime - 23 ms
# Beats 97.47%

# Memory - 13.9 MB
# Beats 50.57%

# Time Complexity - O(n)
# Space Complexity - O(n)
"""

def preorderTraversal(root):
    stack = [root]
    order = []

    while stack:
        node = stack.pop()

        if node:
            order.append(node.val)
            stack.append(node.right)
            stack.append(node.left)

    return order