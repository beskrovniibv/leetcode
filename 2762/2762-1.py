#! /usr/bin/python python

from typing import List


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        pass


def main():
    examples = (
        (
            [5, 4, 2, 4], 8
        ),
        (
            [1, 2, 3], 6
        )
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, expected = example
        got = solution.continuousSubarrays(
            nums=nums
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
