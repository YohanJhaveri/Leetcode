"""
# Runtime - 37 ms
# Beats 62.38%

# Memory - 13.7 MB
# Beats 97.79%

# Time Complexity - O(n^2)
# Space Complexity - O(n)
"""

def getRow(rowIndex):
    if rowIndex == 0:
        return [1]

    if rowIndex == 1:
        return [1, 1]

    row = [1, 1]

    for _ in range(rowIndex - 1):
        row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]

    return row
