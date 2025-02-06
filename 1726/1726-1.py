#! /usr/bin/env python

from typing import List


class Solution:
    def tupleSameProduct(self,  nums: List[int]) -> int:
        pass


def main():
    examples = (
        (
            [2, 3, 4, 6], 8
        ),
        (
            [1, 2, 4, 5, 10], 16
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, expected = example
        got = solution.tupleSameProduct(
            nums=nums,
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
