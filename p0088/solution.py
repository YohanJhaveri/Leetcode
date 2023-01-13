"""
# Runtime - 44 ms
# Beats 62.63%

# Memory - 13.9 MB
# Beats 82.58%

# Time Complexity - O(m + n)
# Space Complexity - O(1)
"""

def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """

    i = m - 1
    j = n - 1
    k = m + n - 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1

        else:
            nums1[k] = nums2[j]
            j -= 1

        k -= 1

    if j >= 0:
        nums1[:j + 1] = nums2[:j + 1]