"""
# Runtime - 597 ms
# Beats 97.39%

# Memory - 27.2 MB
# Beats 48.45%

# Time Complexity - O(n)
# Space Complexity - O(n)
"""

def containsNearbyDuplicate(nums, k):
    seen = {}

    for i, n in enumerate(nums):
        if n in seen and abs(seen[n] - i) <= k:
            return True

        seen[n] = i

    return False