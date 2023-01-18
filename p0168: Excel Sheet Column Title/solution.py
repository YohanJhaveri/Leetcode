"""
# Runtime - 26 ms
# Beats 94.25%

# Memory - 13.9 MB
# Beats 54.80%

# Time Complexity - O(log(n))
# Space Complexity - O(1)
"""

def convertToTitle(columnNumber):
    position = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    title = ""

    while columnNumber:
        title = position[(columnNumber - 1) % 26] + title
        columnNumber = (columnNumber - 1) // 26

    return title