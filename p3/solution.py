"""
# Runtime - 86 ms
# Beats 76.34%

# Memory - 14 MB
# Beats 50.81%

# Time Complexity - O(n)
# Space Complexity - O(n)
"""

def lengthOfLongestSubstring(s):
    n = len(s)

    cur_length = 0
    max_length = 0

    seen = set()

    i = 0
    j = 0

    while j < n:
        if s[j] in seen:
            seen.remove(s[i])
            i += 1
            cur_length -= 1
        else:
            seen.add(s[j])
            j += 1
            cur_length += 1

        max_length = max(max_length, cur_length)

    return max_length