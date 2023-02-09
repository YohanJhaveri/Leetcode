"""
# Runtime - 97 ms
# Beats 47.40%

# Memory - 14.9 MB
# Beats 12.83%

# Time Complexity - O(m * n)
# Space Complexity - O(1)
"""

def matrixReshape(mat, r, c):
    m = len(mat)
    n = len(mat[0])

    if m * n != r * c:
        return mat

    ans = [[[0] for i in range(c)] for j in range(r)]

    for i in range(m):
        for j in range(n):
            e = i * n + j

            x = e // c
            y = e % c

            ans[x][y] = mat[i][j]

    return ans