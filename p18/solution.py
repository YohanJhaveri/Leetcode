"""
# Runtime - 1191 ms
# Beats 57.12%

# Memory - 13.9 MB
# Beats 64.36%

# Time Complexity - O(n^3)
# Space Complexity - O(1)
"""

def fourSum(nums, target):
    nums.sort()
    n = len(nums)

    answers = set()

    for i in range(n):
        ni = nums[i]

        for j in range(i + 1, n):
            nj = nums[j]

            l = j + 1
            r = n - 1

            while l < r:
                nl = nums[l]
                nr = nums[r]

                total = ni + nj + nl + nr

                if total < target:
                    l += 1
                    continue

                if total > target:
                    r -= 1
                    continue

                answers.add((ni, nj, nl, nr))
                l += 1
                r -= 1

    return answers