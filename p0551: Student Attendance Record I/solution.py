"""
# Runtime - 31 ms
# Beats 75.49%

# Memory - 13.8 MB
# Beats 94.74%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

def checkRecord(s):
    n = len(s)
    a = 0

    for i in range(n):
        if i - 2 >= 0 and {s[i], s[i-1], s[i-2]} == {"L"}:
            return False

        if s[i] == "A":
            a += 1

        if a == 2:
            return False

    return True
