"""
# Runtime - 769 ms
# Beats 85.69%

# Memory - 17.2 MB
# Beats 92.91%

# Time Complexity - O(n^2)
# Space Complexity - O(1)
"""

def threeSum(nums):
    nums.sort()
    n = len(nums)

    answers = set()

    for i, ni in enumerate(nums):
        # Skip when current number is the same as previous number
        if i > 0 and ni == nums[i - 1]:
            continue

        l = i + 1
        r = n - 1

        while l < r:
            nl = nums[l]
            nr = nums[r]

            total = ni + nl + nr

            if total < 0:
                l += 1
                continue

            if total > 0:
                r -= 1
                continue

            answers.add((ni, nl, nr))

            l += 1
            r -= 1

    return answers