"""
# Runtime - 99 ms
# Beats 93.23%

# Memory - 15.1 MB
# Beats 29.48%

# Time Complexity - O(m * n)
# Space Complexity - O(m + n)
"""

def isSubtree(root, subRoot):
    def isSameTree(nodeA, nodeB):
        if not nodeA and not nodeB:
            return True

        if nodeA and nodeB:
            return nodeA.val == nodeB.val and isSameTree(nodeA.left, nodeB.left) and isSameTree(nodeA.right, nodeB.right)

        return False


    def recurse(node):
        if node:
            return recurse(node.left) or recurse(node.right) or isSameTree(node, subRoot)

        return False

    return recurse(root)
