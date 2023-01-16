"""
# Runtime - 61 ms
# Beats 87.21%

# Memory - 15.5 MB
# Beats 79.17%

# Time Complexity - O(n*log(n))
# Space Complexity - O(n)
"""

def sortedArrayToBST(nums):
    def aux(l, r):
        if l > r:
            return None

        mid = (l + r) // 2

        node = TreeNode(nums[mid])
        node.left = aux(l, mid - 1)
        node.right = aux(mid + 1, r)

        return node

    return aux(0, len(nums) - 1)