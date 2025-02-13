#! /usr/bin/env python

from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        pass


def main():
    examples = (
        (
            [2, 11, 10, 1, 3], 10, 2
        ),
        (
            [1, 1, 2, 4, 9], 20, 4
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, k, expected = example
        got = solution.minOperations(
            nums=nums,
            k=k
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
