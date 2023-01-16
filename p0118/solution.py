"""
# Runtime - 39 ms
# Beats 55.10%

# Memory - 13.7 MB
# Beats 97.79%

# Time Complexity - O(n^2)
# Space Complexity - O(n^2)
"""

def generate(numRows):
    if numRows == 1:
        return [[1]]

    if numRows == 2:
        return [[1], [1, 1]]

    rows = [[1], [1, 1]]

    for _ in range(numRows - 2):
        prevRow = rows[-1]
        nextRow = [1] + [prevRow[i] + prevRow[i + 1] for i in range(len(prevRow) - 1)] + [1]

        rows.append(nextRow)

    return rows