#! /usr/bin/env python

from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        pass


def main():
    examples = (
        (
            [4, 2, 4, 5, 6], 17
        ),
        (
            [5, 2, 1, 2, 5, 2, 1, 2, 5], 8
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, expected = example
        got = solution.maximumUniqueSubarray(
            nums=nums,
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
