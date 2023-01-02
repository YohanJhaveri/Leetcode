"""
# Runtime - 43 ms
# Beats 99.49%

# Memory - 14 MB
# Beats 51.65%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

def convert(s, numRows):
    n = len(s)

    if numRows == 1:
        return s

    result = ""
    spacingT = (numRows - 1) * 2

    for i in range(numRows):
        index = i

        # First and last row
        if i == 0 or i == numRows - 1:
            while index < n:
                result += s[index]
                index += spacingT


        # Middle rows
        else:
            spacingA = spacingT - (i * 2)
            spacingB = (i * 2)

            flag = True

            while index < n:
                result += s[index]
                index += spacingA if flag else spacingB
                flag = not flag

    return result