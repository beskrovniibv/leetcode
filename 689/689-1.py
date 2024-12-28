#! /usr/bin/python python python3

from typing import List


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        pass


def main():
    examples = (
        (
            [1, 2, 1, 2, 6, 7, 5, 1], 2, [0, 3, 5]
        ),
        (
            [1, 2, 1, 2, 1, 2, 1, 2, 1], 2, [0, 2, 4]
        ),
    )
    solution = Solution()
    for idx, example in examples:
        nums, k, expected = example
        got = solution.maxSumOfThreeSubarrays(
            nums=nums,
            k=k
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
