#! /usr/bin/env python

from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        pass


def main():
    examples = (
        (
            [3, 2, 3, 2, 2, 2], True
        ),
        (
            [1, 2, 3, 4], False
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, expected = example
        got = solution.divideArray(
            nums=nums
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
