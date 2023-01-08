"""
# Runtime - 30 ms
# Beats 92.28%

# Memory - 13.8 MB
# Beats 97.99%

# Time Complexity - O(n * k * log(k))
# Space Complexity - O(1)
"""

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def swapPairs(head):
    if not (head and head.next):
        return head

    dummy = ListNode(0, head)

    prevNode = dummy
    currNode = head

    while currNode and currNode.next:
        prevNode.next = currNode.next
        currNode.next = prevNode.next.next
        prevNode.next.next = currNode
        prevNode = currNode
        currNode = currNode.next

    return dummy.next