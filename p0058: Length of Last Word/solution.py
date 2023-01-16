"""
# Runtime - 35 ms
# Beats 99.95%

# Memory - 14.7 MB
# Beats 37.95%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

def lengthOfLastWord(s):
    n = len(s)
    i = n - 1
    w = 0

    flag = False

    while i >= 0:
        if s[i] == " ":
            if flag:
                return w

        else:
            flag = True
            w += 1

        i -= 1

    return w