"""
# Runtime - 890 ms
# Beats 71.64%

# Memory - 14 MB
# Beats 59.66%

# Time Complexity - O(n^2)
# Space Complexity - O(1)
"""

def longestPalindrome(s):
    n = len(s)
    max_palindrome = ""

    for index in range(n):
        # ODD
        offset = 1
        palindrome = s[index]

        while True:
            l = index - offset
            r = index + offset

            if l < 0 or r >= n:
                break

            if s[l] != s[r]:
                break

            palindrome = s[l] + palindrome + s[r]
            offset += 1

        max_palindrome = max(max_palindrome, palindrome, key=len)


        # EVEN
        offset = 0
        palindrome = ""

        while True:
            l = index - offset
            r = index + offset + 1

            if l < 0 or r >= n:
                break

            if s[l] != s[r]:
                break

            palindrome = s[l] + palindrome + s[r]
            offset += 1

        max_palindrome = max(max_palindrome, palindrome, key=len)

    return max_palindrome
