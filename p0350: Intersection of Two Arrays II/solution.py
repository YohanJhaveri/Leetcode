"""
# Runtime - 59 ms
# Beats 51.91%

# Memory - 14.2 MB
# Beats 13.24%

# Time Complexity - O(m + n)
# Space Complexity - O(m + n)
"""

def intersect(nums1, nums2):
    freq1 = {}
    freq2 = {}
    keys = set()
    ans = []

    for x in nums1:
        freq1[x] = freq1.setdefault(x, 0) + 1
        keys.add(x)

    for x in nums2:
        freq2[x] = freq2.setdefault(x, 0) + 1
        keys.add(x)

    for x in keys:
        ans += [x] * min(freq1.get(x, 0), freq2.get(x, 0))

    return ans