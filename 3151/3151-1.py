#! /usr/bin/env python

from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        pass


def main():
    examples = (
        (
            [1], True
        ),
        (
            [2, 1, 4], True
        ),
        (
            [4, 3, 1, 6], False
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, expected = example
        got = solution.isArraySpecial(
            nums=nums
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
