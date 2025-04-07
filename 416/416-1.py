#! /usr/bin/env python

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        pass


def main():
    examples = (
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
