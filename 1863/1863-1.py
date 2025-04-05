#! /usr/bin/env python

from itertools import combinations
from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        for l in range(len(nums) + 1):
            for s in combinations(nums, r=l):
                t = 0
                for e in s:
                    t ^= e
                result += t
        return result


def main():
    examples = (
        (
            [1, 3], 6
        ),
        (
            [5, 1, 6], 28
        ),
        (
            [3, 4, 5, 6, 7, 8], 480
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, expected = example
        got = solution.subsetXORSum(
            nums=nums
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
