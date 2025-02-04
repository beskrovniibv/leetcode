#! /usr/bin/env python

from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        t = nums[0]
        result = t
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                t += nums[i]
            else:
                t = nums[i]
            result = max(result, t)
        return result


def main():
    examples = (
        (
            [100, 10, 1], 100
        ),
        (
            [10, 20, 30, 5, 10, 50], 65
        ),
        (
            [10, 20, 30, 40, 50], 150
        ),
        (
            [12, 17, 15, 13, 10, 11, 12], 33
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, expected = example
        got = solution.maxAscendingSum(
            nums=nums
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
