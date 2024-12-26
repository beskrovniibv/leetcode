#! /usr/bin/python python

from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        if total_sum < target or (total_sum - target) % 2 != 0:
            return 0
        subset_sum = (total_sum - target) // 2
        dp = [0] * (subset_sum + 1)
        dp[0] = 1
        for num in nums:
            for j in range(subset_sum, num - 1, -1):
                dp[j] += dp[j - num]
        return dp[-1]


def main():
    examples = (
        (
            [1, 1, 1, 1, 1], 3, 5
        ),
        (
            [1],  1,  1
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, target, expected = example
        got = solution.findTargetSumWays(
            nums=nums,
            target=target
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
