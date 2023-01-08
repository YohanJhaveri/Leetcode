"""
# Runtime - 136 ms
# Beats 67.42%

# Memory - 17.8 MB
# Beats 50.76%

# Time Complexity - O(n * k * log(k))
# Space Complexity - O(1)
"""

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    n = len(lists)

    if n == 0:
        return None

    if n == 1:
        return lists[0]

    h = n // 2

    L1 = self.mergeKLists(lists[:h])
    L2 = self.mergeKLists(lists[h:])

    return self.merge2Lists(L1, L2)


def merge2Lists(list1, list2):
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

    if list1:
        list3.next = list1

    if list2:
        list3.next = list2

    return dummy.next