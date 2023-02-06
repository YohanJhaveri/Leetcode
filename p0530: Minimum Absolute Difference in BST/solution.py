"""
# Runtime - 74 ms
# Beats 26.10%

# Memory - 15.9 MB
# Beats 76.31%

# Time Complexity - O(n)
# Space Complexity - O(n)
"""

def getMinimumDifference(root):
    minDiff = float("inf")
    stack = [(root, False)]
    prev = None

    while stack:
        node, visited = stack.pop()

        if visited:
            if prev != None:
                minDiff = min(minDiff, node.val - prev)
            prev = node.val

        elif node:
            stack.append((node.right, False))
            stack.append((node, True))
            stack.append((node.left, False))


    return minDiff