"""
# Runtime - 35 ms
# Beats 85.81%

# Memory - 13.8 MB
# Beats 70.92%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)

    node1 = dummy
    node2 = dummy

    for i in range(n):
        node1 = node1.next

    while node1 != None and node1.next != None:
        node1 = node1.next
        node2 = node2.next

    if node2.next != None:
        node2.next = node2.next.next

    return dummy.next