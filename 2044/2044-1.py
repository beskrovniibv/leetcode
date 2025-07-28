#! /usr/bin/env python

from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        pass


def main():
    examples = (
        (
            [3, 1], 2
        ),
        (
            [2, 2, 2], 7
        ),
        (
            [3, 2, 1, 5], 6
        )
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, expected = example
        got = solution.countMaxOrSubsets(
            nums=nums,
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
