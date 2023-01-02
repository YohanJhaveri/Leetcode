"""
# Runtime - 85 ms
# Beats 98.88%

# Memory - 14.3 MB
# Beats 24.12%

# Time Complexity - O(log(min(m, n)))
# Space Complexity - O(1)
"""

def findMedianSortedArrays(nums1, nums2):
    # makes sure that nums1 is the shorter array
    m = len(nums1)
    n = len(nums2)

    if m > n:
        nums1, nums2 = nums2, nums1
        m, n = n, m

    l = 0
    r = m - 1

    while True:
        p1 = (l + r) // 2
        p2 = (m + n) // 2 - (p1 + 1) - 1

        p1left = nums1[p1] if p1 >= 0 else float("-inf")
        p2left = nums2[p2] if p2 >= 0 else float("-inf")
        p1right = nums1[p1 + 1] if p1 + 1 < m else float("inf")
        p2right = nums2[p2 + 1] if p2 + 1 < n else float("inf")

        if p1left > p2right:
            r = p1 - 1
            continue

        if p2left > p1right:
            l = p1 + 1
            continue

        if (m + n) % 2:
            return min(p1right, p2right)
        
        return (max(p1left, p2left) + min(p1right, p2right)) / 2