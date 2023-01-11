"""
# Runtime - 39 ms
# Beats 67.14%

# Memory - 13.9 MB
# Beats 10.83%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

def addBinary(a, b):
    ai = len(a) - 1
    bi = len(b) - 1

    c = 0
    r = ""

    if a == "0" and b == "0":
        return "0"

    while not (ai < 0 and bi < 0 and c == 0):
        ad = int(a[ai]) if ai >= 0 else 0
        bd = int(b[bi]) if bi >= 0 else 0

        t = (ad + bd + c) % 2
        c = (ad + bd + c) // 2

        r = str(t) + r

        ai -= 1
        bi -= 1

    return r