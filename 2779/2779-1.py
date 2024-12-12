#! /usr/bin/python python

from typing import List


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        l, r = 0, 0
        ans = 0
        while l < n and r < n:
            while r < n and (nums[r] - nums[l] <= 2*k):
                ans = max(ans, r - l + 1)
                r += 1
            l += 1
        return ans


def main():
    examples = (
        (
            [4, 6, 1, 2],
            2,
            3
        ),
        (
            [1, 1, 1, 1],
            10,
            4
        )
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, k, expected = example
        got = solution.maximumBeauty(
            nums=nums,
            k=k
        )
        assert got == expected, f"Error in sample: {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
