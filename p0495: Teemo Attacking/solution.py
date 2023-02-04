"""
# Runtime - 270 ms
# Beats 63.53%

# Memory - 15.5 MB
# Beats 38.58%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

def findPoisonedDuration(timeSeries, duration):
    n = len(timeSeries)
    s = n * duration

    for i in range(n - 1):
        s -= max(0, duration - (timeSeries[i + 1] - timeSeries[i]))

    return s