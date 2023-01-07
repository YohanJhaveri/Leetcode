"""
# Runtime - 30 ms
# Beats 98.90%

# Memory - 13.8 MB
# Beats 99.14%

# Time Complexity - O(m + n)
# Space Complexity - O(m + n)
"""

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    dummy = ListNode()
    list3 = dummy

    while list1 and list2:
        if list1.val < list2.val:
            list3.next = list1
            list1 = list1.next

        else:
            list3.next = list2
            list2 = list2.next

        list3 = list3.next

    if list1: list3.next = list1
    if list2: list3.next = list2

    return dummy.next