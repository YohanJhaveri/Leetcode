"""
# Runtime - 41 ms
# Beats 65.96%

# Memory - 14 MB
# Beats 25.10%

# Time Complexity - O(max(m, n))
# Space Complexity - O(1)
"""

def addStrings(num1, num2):
    n1 = len(num1)
    n2 = len(num2)

    m = max(n1, n2)
    c = 0

    num3 = ""

    for x in range(m):
        i1 = n1 - x - 1
        i2 = n2 - x - 1

        d1 = int(num1[i1]) if i1 >= 0 else 0
        d2 = int(num2[i2]) if i2 >= 0 else 0

        t = d1 + d2 + c

        d3 = t % 10
        c = t // 10

        num3 = str(d3) + num3

    return (str(c) if c else "") + num3
