"""
# Runtime - 473 ms
# Beats 72.56%

# Memory - 25.9 MB
# Beats 68.85%

# Time Complexity - O(n)
# Space Complexity - O(n)
"""

def containsDuplicate(nums):
    seen = set()

    for n in nums:
        if n in seen:
            return True

        seen.add(n)

    return False