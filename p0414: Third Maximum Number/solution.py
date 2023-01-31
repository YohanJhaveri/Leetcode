"""
# Runtime - 54 ms
# Beats 77.69%

# Memory - 14.7 MB
# Beats 99.34%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

def thirdMax(nums):
    m1 = float("-inf")
    m2 = float("-inf")
    m3 = float("-inf")

    for n in nums:
        if n in {m1, m2, m3}:
            continue

        elif n > m1:
            m3 = m2
            m2 = m1
            m1 = n

        elif n > m2:
            m3 = m2
            m2 = n

        elif n > m3:
            m3 = n

    return m3 if m3 != float("-inf") else m1