"""
# Runtime - 53 ms
# Beats 82.14%

# Memory - 15 MB
# Beats 54.39%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

def reverseVowels(s):
    l = 0
    r = len(s) - 1

    vowels = set("aeiou")
    letters = list(s)

    while l < r:
        if s[l].lower() not in vowels:
            l += 1
            continue

        if s[r].lower() not in vowels:
            r -= 1
            continue

        letters[l], letters[r] = letters[r], letters[l]
        l += 1
        r -= 1

    return "".join(letters)
