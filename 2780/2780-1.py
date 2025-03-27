#! /usr/bin/env python

from typing import List


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        pass


def main():
    examples = (
        (
            [1, 2, 2, 2], 2
        ),
        (
            [2, 1, 3, 1, 1, 1, 7, 1, 2, 1], 4
        ),
        (
            [3, 3, 3, 3, 7, 2, 2], -1
        )
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, expected = example
        got = solution.minimumIndex(
            nums=nums
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
