#! /usr/bin/env python

from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        pass


def main():
    examples = (
        (
            [1, 0, 1], [[0, 2]], True
        ),
        (
            [4, 3, 2, 1], [[1, 3], [0, 2]], False
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, queries, expected = example
        got = solution.isZeroArray(
            nums=nums,
            queries=queries
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
