#! /usr/bin/env python

from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        pass


def main():
    examples = (
        (
            [1, -3, 2, 3, -4], 5
        ),
        (
            [2, -5, 1, -4, 3, -2], 8
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, expected = example
        got = solution.maxAbsoluteSum(
            nums=nums
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
