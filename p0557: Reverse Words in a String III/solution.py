"""
# Runtime - 66 ms
# Beats 37.29%

# Memory - 14.5 MB
# Beats 78.41%

# Time Complexity - O(n)
# Space Complexity - O(n)
"""

def reverseWords(s):
    n = len(s)
    words = s.split(" ")

    for i, word in enumerate(words):
        if word == "":
            continue

        letters = list(word)
        slow = 0
        fast = len(word) - 1

        while slow < fast:
            letters[slow], letters[fast] = letters[fast], letters[slow]
            slow += 1
            fast -= 1

        words[i] = "".join(letters)

    return " ".join(words)
