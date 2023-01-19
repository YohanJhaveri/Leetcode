"""
# Runtime - 75 ms
# Beats 69.2%

# Memory - 17.7 MB
# Beats 80.66%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

def removeElements(head, val):
    dummy = ListNode(0, head)
    node = dummy

    while node and node.next:
        if node.next.val == val:
            node.next = node.next.next
        else:
            node = node.next

    return dummy.next