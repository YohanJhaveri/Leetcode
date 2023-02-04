"""
# Runtime - 34 ms
# Beats 54.54%

# Memory - 13.8 MB
# Beats 60.7%

# Time Complexity - O(m * n)
# Space Complexity - O(1)
"""

def findWords(words):
    r1 = set("qwertyuiop")
    r2 = set("asdfghjkl")
    r3 = set("zxcvbnm")

    ans = []

    for word in words:
        letters = set(word.lower())

        if letters - r1 == set() or letters - r2 == set() or letters - r3 == set():
            ans.append(word)

    return ans
