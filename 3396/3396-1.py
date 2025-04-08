#! /usr/bin/env python

from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        pass


def main():
    examples = (
        (
            [1, 2, 3, 4, 2, 3, 3, 5, 7], 2
        ),
        (
            [4, 5, 6, 4, 4], 2
        ),
        (
            [6, 7, 8, 9], 0
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, expected = example
        got = solution.minimumOperations(
            nums=nums
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
