#! /usr/bin/env python

from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        pass


def main():
    examples = (
        (
            [1, 2, 2, 1, 1, 0], [1, 4, 2, 0, 0, 0]
        ),
        (
            [0, 1], [1, 0]
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, expected = example
        got = solution.applyOperations(
            nums=nums
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
