"""
# Runtime - 24 ms
# Beats 97.79%

# Memory - 13.9 MB
# Beats 11.31%

# Time Complexity - O(n)
# Space Complexity - O(n)
"""

def isSameTree(p, q):
    return (not p and not q) or (p and q and p.val == q.val) and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)