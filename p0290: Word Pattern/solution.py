"""
# Runtime - 34 ms
# Beats 50.76%

# Memory - 13.9 MB
# Beats 61.59%

# Time Complexity - O(n)
# Space Complexity - O(n)
"""

def wordPattern(pattern, s):
    words = s.split(" ")

    wc = {}
    cw = {}

    if len(words) != len(pattern):
        return False

    n = len(pattern)

    for i in range(n):
        word = words[i]
        char = pattern[i]


        we = word in wc
        ce = char in cw

        if not we and not ce:
            wc[word] = char
            cw[char] = word

        elif we and ce:
            if wc[word] != char or cw[char] != word:
                return False

        else:
            return False

    return True