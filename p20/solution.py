"""
# Runtime - 34 ms
# Beats 82.28%

# Memory - 13.9 MB
# Beats 71.3%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

def isValid(self, s: str) -> bool:
    pairs = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    stack = []

    for bracket in s:
        if bracket in pairs:
            if not stack:
                return False

            if pairs[bracket] != stack.pop():
                return False

        else:
            stack.append(bracket)

    return not stack