"""
# Runtime - 33 ms
# Beats 99.19%

# Memory - 13.9 MB
# Beats 68.39%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

def deleteDuplicates(head):
    node = head

    if node == None:
        return None

    while node.next != None:
        if node.val == node.next.val:
            node.next = node.next.next
            continue

        node = node.next

    return head