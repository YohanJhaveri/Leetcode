"""
# Runtime - 39 ms
# Beats 68.30%

# Memory - 14 MB
# Beats 57.68%

# Time Complexity - O(n)
# Space Complexity - O(n)
"""

def isSymmetric(root):
    def isSameTree(p, q):
        return (not p and not q) or (p and q and p.val == q.val) and isSameTree(p.left, q.right) and isSameTree(p.right, q.left)

    return isSameTree(root.left, root.right)