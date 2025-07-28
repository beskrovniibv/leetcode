#! /usr/bin/env python

from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        target = 0
        for v in nums:
            target |= v
        result = 0
        for mask in range(1, 2**n):
            temp = 0
            for idx in range(n):
                i = (mask >> idx) & 1
                if i == 1:
                    temp |= nums[idx]
            if temp == target:
                result += 1
        return result


def main():
    examples = (
        (
            [3, 1], 2
        ),
        (
            [2, 2, 2], 7
        ),
        (
            [3, 2, 1, 5], 6
        )
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, expected = example
        got = solution.countMaxOrSubsets(
            nums=nums,
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
