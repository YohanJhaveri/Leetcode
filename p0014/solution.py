"""
# Runtime - 38 ms
# Beats 80.74%

# Memory - 13.8 MB
# Beats 87.44%

# Time Complexity - O(m*n)
# Space Complexity - O(m)
"""

def longestCommonPrefix(strs):
    shortest = min(strs, key=len)
    result = ""

    for index, character in enumerate(shortest):
        for string in strs:
            if string[index] != character:
                return result

        result += character

    return result