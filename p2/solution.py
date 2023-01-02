"""
# Runtime - 61 ms
# Beats 98.6%

# Memory - 13.8 MB
# Beats 86.24%

# Time Complexity - O(n)
# Space Complexity - O(n)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    carry = 0
    dummy = ListNode(0)
    l3 = dummy

    while l1 or l2 or carry:
        total = 0
        
        if l1:
            total += l1.val
            l1 = l1.next
        
        if l2:
            total += l2.val
            l2 = l2.next

        if carry:
            total += carry

        value = total % 10
        carry = total // 10

        l3.next = ListNode(value)
        l3 = l3.next

    return dummy.next