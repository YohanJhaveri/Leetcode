"""
# Runtime - 46 ms
# Beats 92.11%

# Memory - 14 MB
# Beats 30.7%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

def romanToInt(s):
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

    num = 0

    n = len(s)
    i = 0

    while i < n:
        double = s[i:i+2]
        single = s[i]

        if double in value:
            num += value[double]
            i += 2
        else:
            num += value[single]
            i += 1

    return num
