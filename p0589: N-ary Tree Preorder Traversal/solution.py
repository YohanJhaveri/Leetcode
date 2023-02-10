"""
# Runtime - 58 ms
# Beats 41.95%

# Memory - 16 MB
# Beats 76.59%

# Time Complexity - O(n)
# Space Complexity - O(n)
"""

def preorder(root):
    stack = [(root, False)]
    order = []

    while stack:
        node, visited = stack.pop()

        if visited:
            order.append(node.val)
        elif node:
            for child in node.children[::-1]:
                stack.append((child, False))

            stack.append((node, True))

    return order