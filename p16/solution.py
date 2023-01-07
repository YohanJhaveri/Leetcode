"""
# Runtime - 1450 ms
# Beats 55.82%

# Memory - 14 MB
# Beats 23.40%

# Time Complexity - O(n^2)
# Space Complexity - O(1)
"""

def threeSumClosest(nums, target):
    nums.sort()
    n = len(nums)

    answer = float("inf")

    for i, ni in enumerate(nums):
        if i > 0 and ni == nums[i - 1]:
            continue

        l = i + 1
        r = n - 1

        while l < r:
            nl = nums[l]
            nr = nums[r]

            total = ni + nl + nr

            if answer == float("inf") or abs(target - total) < abs(target - answer):
                answer = total

            if target > total:
                l += 1
                continue

            if target < total:
                r -= 1
                continue

            l += 1
            r -= 1

    return answer