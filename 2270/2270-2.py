#! /usr/bin/python python python3

from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        psum = nums[0]
        result = 0
        for i in range(1, n):
            l = psum
            r = total - psum
            if l >= r:
                result += 1
            psum += nums[i]
        return result


def main():
    examples = (
        (
            [10, 4, -8, 7], 2
        ),
        (
            [2, 3, 1, 0], 2
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, expected = example
        got = solution.waysToSplitArray(
            nums=nums
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
