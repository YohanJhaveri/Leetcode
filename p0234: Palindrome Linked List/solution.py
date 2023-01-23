"""
# Runtime - 774 ms
# Beats 85.3%

# Memory - 39 MB
# Beats 86.1%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

def isPalindrome(head):
    isEven = None

    node = head
    size = 0

    while node:
        node = node.next
        size += 1

    isOdd = size % 2

    half = (size // 2) + isOdd

    node = head

    for i in range(half):
        node = node.next

    prv = None
    cur = node

    while cur:
        nxt = cur.next
        cur.next = prv
        prv = cur
        cur = nxt

    while prv:
        if prv.val != head.val:
            return False

        prv = prv.next
        head = head.next

    return True