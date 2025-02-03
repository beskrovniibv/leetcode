#! /usr/bin/env python

from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        mns = [1]*n
        mxs = [1]*n
        mx, mn = 1, 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                mxs[i] = mxs[i - 1] + 1
                mx = max(mx, mxs[i])
            if nums[i] < nums[i - 1]:
                mns[i] = mns[i - 1] + 1
                mn = max(mn, mns[i])
        return max(mx, mn)


def main():
    examples = (
        (
            [1, 4, 3, 3, 2], 2
        ),
        (
            [3, 3, 3, 3], 1
        ),
        (
            [3, 2, 1], 3
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, expected = example
        got = solution.longestMonotonicSubarray(
            nums=nums
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
