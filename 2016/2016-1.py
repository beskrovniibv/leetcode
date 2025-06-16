#! /usr/bin/env python

from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, 1
        mx = -1
        while r < n:
            d = nums[r] - nums[l] if nums[l] < nums[r] else -1
            mx = max(mx, d)
            if nums[r] < nums[l]:
                l = r
                r = l + 1
                continue
            r += 1
        return mx


def main():
    examples = (
        (
            [7, 1, 5, 4], 4
        ),
        (
            [9, 4, 3, 2], -1
        ),
        (
            [1, 5, 2, 10], 9
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, expected = example
        got = solution.maximumDifference(
            nums=nums,
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}"


if __name__ == "__main__":
    main()
