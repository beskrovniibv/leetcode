#! /usr/bin/env python

from typing import List


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        f1, f2 = {}, {}
        for num in nums:
            f1[num] = f1.get(num, 0) + 1
        for i, num in enumerate(nums):
            f1[num] -= 1
            f2[num] = f2.get(num, 0) + 1
            if f2[num]*2 > i + 1 and f1[num]*2 > n - i - 1:
                return i
        return -1


def main():
    examples = (
        (
            [1, 2, 2, 2], 2
        ),
        (
            [2, 1, 3, 1, 1, 1, 7, 1, 2, 1], 4
        ),
        (
            [3, 3, 3, 3, 7, 2, 2], -1
        )
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, expected = example
        got = solution.minimumIndex(
            nums=nums
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
