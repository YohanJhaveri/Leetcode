"""
# Runtime - 59 ms
# Beats 35.79%

# Memory - 16 MB
# Beats 80.36%

# Time Complexity - O(n)
# Space Complexity - O(n)
"""

def postorder(root):
    stack = [(root, False)]
    order = []

    while stack:
        node, visited = stack.pop()

        if visited:
            order.append(node.val)
        elif node:
            stack.append((node, True))

            for child in node.children[::-1]:
                stack.append((child, False))

    return order