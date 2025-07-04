#! /usr/bin/env python

from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = 1
        nums.sort()
        i = 0
        mn, mx = nums[i], nums[i]
        while i < n:
            if nums[i] > mx:
                mx = nums[i]
            if mx - mn > k:
                mn = nums[i]
                result += 1
            i += 1
        return result


def main():
    examples = (
        (
            [3, 6, 1, 2, 5], 2, 2
        ),
        (
            [1, 2, 3], 1, 2
        ),
        (
            [2, 2, 4, 5], 0, 3
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, k, expected = example
        got = solution.partitionArray(
            nums=nums,
            k=k,
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}"


if __name__ == "__main__":
    main()
