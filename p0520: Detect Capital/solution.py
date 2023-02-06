"""
# Runtime - 26 ms
# Beats 95.43%

# Memory - 13.9 MB
# Beats 6.78%

# Time Complexity - O(n)
# Space Complexity - O(n)
"""

def detectCapitalUse(word):
    if word == word.upper():
        return True

    if word[1:] == word[1:].lower():
        return True

    return False