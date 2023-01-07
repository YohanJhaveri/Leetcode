"""
# Runtime - 19 ms
# Beats 99.90%

# Memory - 13.9 MB
# Beats 78.37%

# Time Complexity - O(n^4)
# Space Complexity - O(1)
"""

def letterCombinations(self, digits: str) -> List[str]:
    letters = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    combos = []
    n = len(digits)

    d1 = letters[digits[0]] if n > 0 else [None]
    d2 = letters[digits[1]] if n > 1 else [None]
    d3 = letters[digits[2]] if n > 2 else [None]
    d4 = letters[digits[3]] if n > 3 else [None]

    # Since the length of `digits` is between 0 and 4
    for d in d4:
        for c in d3:
            for b in d2:
                for a in d1:
                    if a == None:
                        return []

                    if b == None:
                        combos.append(d)
                        continue

                    if c == None:
                        combos.append(c + d)
                        continue

                    if d == None:
                        combos.append(b + c + d)
                        continue

                    combos.append(a + b + c + d)


    return combos