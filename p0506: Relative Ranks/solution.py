"""
# Runtime - 73 ms
# Beats 78.67%

# Memory - 15.2 MB
# Beats 54.59%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

def findRelativeRanks(score):
    order = sorted(score)[::-1]
    hashmap = {}
    podium = ["Gold Medal", "Silver Medal", "Bronze Medal"]
    answer = []

    for i, x in enumerate(order):
        hashmap[x] = podium[i] if i < 3 else str(i + 1)

    for x in score:
        answer.append(hashmap[x])

    return answer