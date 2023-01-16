"""
# Runtime - 52 ms
# Beats 83.3%

# Memory - 14.2 MB
# Beats 13.57%

# Time Complexity - O(sn * pn)
# Space Complexity - O(sn * pn)
"""

def isMatch(s, p):
    sn = len(s)
    pn = len(p)

    nodes = []
    pi = 0
    si = 0

    while pi < pn:
        if pi + 1 < pn and p[pi + 1] == "*":
            nodes.append(p[pi] + "*")
            pi += 2
            continue

        nodes.append(p[pi])
        pi += 1


    cache = {}

    def aux(ni, si):
        ans = ni == len(nodes) or all([len(nodes[i]) == 2 for i in range(ni, len(nodes))])

        if si < sn:
            if (ni, si) in cache:
                return cache[(ni, si)]

            if ni == len(nodes):
                ans = False

            elif len(nodes[ni]) == 1:
                if nodes[ni][0] in [s[si], "."]:
                    ans = aux(ni + 1, si + 1) # one
                else:
                    ans = False

            else:
                if nodes[ni][0] in [s[si], "."]:
                    m = aux(ni, si + 1) # multiple
                    o = aux(ni + 1, si + 1) # one
                    z = aux(ni + 1, si) # zero

                    ans = m or o or z
                else:
                    ans = aux(ni + 1, si) # zero

            cache[(ni, si)] = ans

        return ans

    return aux(0, 0)