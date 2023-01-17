"""
# Runtime - 28 ms
# Beats 90.64%

# Memory - 13.9 MB
# Beats 10.67%

# Time Complexity - O(n)
# Space Complexity - O(n)
"""

def postorderTraversal(root):
    stack = [root]
    order = []

    while stack:
        node = stack.pop()

        if node:
            order.append(node.val)
            stack.append(node.left)
            stack.append(node.right)

    return order[::-1]