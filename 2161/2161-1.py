#! /usr/bin/env python

from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        pass


def main():
    examples = (
        (
            [9, 12, 5, 10, 14, 3, 10], 10, [9, 5, 3, 10, 10, 12, 14]
        ),
        (
            [-3, 4, 3, 2], 2, [-3, 2, 4, 3]
        ),
    )
    solution = Solution()
    for idx, exmaple in enumerate(examples):
        nums, pivot, expected = exmaple
        got = solution.pivotArray(
            nums=nums,
            pivot=pivot
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
