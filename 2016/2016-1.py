#! /usr/bin/env python

from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        pass


def main():
    examples = (
        (
            [7,1,5,4], 4
        ),
        (
            [9,4,3,2], -1
        ),
        (
            [1,5,2,10], 9
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, expected = example
        got = solution.maximumDifference(
            nums=nums,
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}"


if __name__ == "__main__":
    main()
