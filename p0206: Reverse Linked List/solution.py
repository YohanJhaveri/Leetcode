"""
# Runtime - 41 ms
# Beats 67.5%

# Memory - 15.4 MB
# Beats 52.93%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

def reverseList(head):
    cur = head
    prv = None

    while cur:
        nxt = cur.next
        cur.next = prv
        prv = cur
        cur = nxt

    return prv