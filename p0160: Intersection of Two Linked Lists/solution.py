"""
# Runtime - 161 ms
# Beats 82.44%

# Memory - 29.7 MB
# Beats 40.47%

# Time Complexity - O(m + n)
# Space Complexity - O(1)
"""

def getIntersectionNode(headA, headB):
    nodeA = headA
    nodeB = headB

    m = 0
    n = 0

    while nodeA:
        nodeA = nodeA.next
        m += 1

    while nodeB:
        nodeB = nodeB.next
        n += 1

    nodeA = headA
    nodeB = headB

    while m > n:
        nodeA = nodeA.next
        m -= 1

    while n > m:
        nodeB = nodeB.next
        n -= 1

    while nodeA:
        if nodeA == nodeB:
            return nodeA

        nodeA = nodeA.next
        nodeB = nodeB.next

    return None