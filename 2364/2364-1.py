#! /usr/bin/env python

from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        diffs = {}
        result = 0
        for i in range(n):
            c = diffs.get(i - nums[i], 0)
            result += i - c
            diffs[i - nums[i]] = c + 1
        return result


def main():
    examples = (
        (
            [4, 1, 3, 3], 5
        ),
        (
            [1, 2, 3, 4, 5], 0
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, expected = example
        got = solution.countBadPairs(
            nums=nums
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
