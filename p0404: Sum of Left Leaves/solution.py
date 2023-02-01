"""
# Runtime - 40 ms
# Beats 44.44%

# Memory - 14.3 MB
# Beats 81.14%

# Time Complexity - O(n)
# Space Complexity - O(n)
"""

def sumOfLeftLeaves(root):
    stack = [root]
    total = 0

    while stack:
        node = stack.pop()

        if node:
            print(node.val)
            if node.left and not node.left.left and not node.left.right:
                total += node.left.val

            stack.append(node.left)
            stack.append(node.right)

    return total