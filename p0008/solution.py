"""
# Runtime - 35 ms
# Beats 90.69%

# Memory - 13.8 MB
# Beats 78.15%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

def myAtoi(s):
    MIN_INTEGER = -(2 ** 31)
    MAX_INTEGER = (2 ** 31) - 1
    DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    is_negative = False
    is_currently_leading = True
    is_digits_seen = False
    is_sign_seen = False

    digits = ""

    for c in s:
        # Ignore leading spaces
        if is_currently_leading and c == " ":
            continue

        # No longer any leading spaces
        is_currently_leading = False

        if c in DIGITS:
            is_digits_seen = True
            digits += c

        elif is_digits_seen:
            break

        elif not is_sign_seen and (c == "+" or c == "-"):
            is_sign_seen = True
            is_negative = c == "-"

        else:
            break

    if digits == "":
        return 0

    number = int(digits) * (-1 if is_negative else 1)

    if number < MIN_INTEGER: return MIN_INTEGER
    if number > MAX_INTEGER: return MAX_INTEGER

    return number