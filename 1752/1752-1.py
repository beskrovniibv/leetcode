#! /usr/bin/env python

from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        pass


def main():
    examples = (
        (
            [3, 4, 5, 1, 2], True
        ),
        (
            [2, 1, 3, 4], False
        ),
        (
            [1, 2, 3], True
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, expected = example
        got = solution.check(
            nums=nums
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
