#! /usr/bin/env python

from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        pos, neg = 0, 0
        for i in range(n):
            if nums[i] < 0:
                neg += 1
            elif nums[i] > 0:
                pos += 1
        return max(pos, neg)


def main():
    examples = (
        (
            [-2, -1, -1, 1, 2, 3], 3
        ),
        (
            [-3, -2, -1, 0, 0, 1, 2], 3
        ),
        (
            [5, 20, 66, 1314], 4
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, expected = example
        got = solution.maximumCount(
            nums=nums,
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
