"""
# Runtime - 29 ms
# Beats 81.33%

# Memory - 13.8 MB
# Beats 92.35%

# Time Complexity - O(n)
# Space Complexity - O(n)
"""

def countSegments(s):
    return len([x for x in s.split(" ") if x != ""])