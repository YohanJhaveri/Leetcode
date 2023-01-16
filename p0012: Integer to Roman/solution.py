"""
# Runtime - 43 ms
# Beats 96.97%

# Memory - 13.9 MB
# Beats 80.31%

# Time Complexity - O(1)
# Space Complexity - O(1)
"""

def intToRoman(num):
    order = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    value = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }

    ans = ""

    for n in order:
        count = num // value[n]

        if count:
            ans += count * n
            num -= count * value[n]

    return ans