#! /usr/bin/env python

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        _sum = sum(nums)
        if _sum & 1 == 1:
            return False
        _half = _sum // 2
        dp = [False]*(_half + 1)
        dp[0] = True
        for num in nums:
            for i in range(_half, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[_half]


def main():
    examples = (
        (
            [14, 9, 8, 4, 3, 2], True
        ),
        (
            [1, 5, 11, 5], True
        ),
        (
            [1, 2, 3, 5], False
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, expected = example
        got = solution.canPartition(
            nums=nums
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."

if __name__ == "__main__":
    main()
