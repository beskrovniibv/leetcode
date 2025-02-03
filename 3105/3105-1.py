#! /usr/bin/env python

from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        pass


def main():
    examples = (
        (
            [1, 4, 3, 3, 2], 2
        ),
        (
            [3, 3, 3, 3], 1
        ),
        (
            [3, 2, 1], 3
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, expected = example
        got = solution.longestMonotonicSubarray(
            nums=nums
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
