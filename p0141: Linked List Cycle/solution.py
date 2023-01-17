"""
# Runtime - 59 ms
# Beats 74.49%

# Memory - 17.4 MB
# Beats 94.82%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

def hasCycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False