"""
# Runtime - 53 ms
# Beats 56.35%

# Memory - 14.2 MB
# Beats 76.55%

# Time Complexity - O(m + n)
# Space Complexity - O(m + n)
"""

def generateParenthesis(n):
    count = 0
    result = []

    def aux(l, r, s):
        if len(s) == n * 2:
            if count == 0:
                result.append(s)
            return

        if l > r:
            aux(l, r + 1, s + ")")

        if l < n:
            aux(l + 1, r, s + "(")

    aux(0, 0, "")

    return result