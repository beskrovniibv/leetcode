#! /usr/bin/env python

from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        pass


def main():
    examples = (
        (
            [18, 43, 36, 13, 7], 54
        ),
        (
            [10, 12, 19, 14], -1
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, expected = example
        got = solution.maximumSum(
            nums=nums
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
