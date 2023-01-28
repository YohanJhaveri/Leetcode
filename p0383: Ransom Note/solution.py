"""
# Runtime - 74 ms
# Beats 50.30%

# Memory - 14.1 MB
# Beats 92.10%

# Time Complexity - O(m + n)
# Space Complexity - O(m + n)
"""

def canConstruct(ransomNote, magazine):
    if len(ransomNote) > len(magazine):
        return False

    letters = {}

    for x in magazine:
        letters[x] = letters.get(x, 0) + 1

    for x in ransomNote:
        if letters.get(x, 0) == 0:
            return False

        letters[x] -= 1

    return True