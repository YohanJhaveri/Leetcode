"""
# Runtime - 51 ms
# Beats 41.82%

# Memory - 15.1 MB
# Beats 13.7%

# Time Complexity - O(n)
# Space Complexity - O(1)
"""

def fizzBuzz(n):
    answers = []

    for x in range(1, n + 1):
        answers.append(("" if x % 3 else "Fizz") + ("" if x % 5 else "Buzz") or str(x))

    return answers