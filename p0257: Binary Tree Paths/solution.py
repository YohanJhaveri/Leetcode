"""
# Runtime - 43 ms
# Beats 40.92%

# Memory - 14.1 MB
# Beats 25.9%

# Time Complexity - O(n)
# Space Complexity - O(n)
"""

def binaryTreePaths(root):
    paths = []

    def traverse(node, path):
        if not (node.left or node.right):
            paths.append(path + str(node.val))

        if node.left:
            traverse(node.left, path + str(node.val) + "->")

        if node.right:
            traverse(node.right, path + str(node.val) + "->")

    traverse(root, "")

    return paths