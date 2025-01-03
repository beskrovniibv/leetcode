#! /usr/bin/python python python3

from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        psum = [0] + [0]*n
        for i in range(1, n + 1):
            psum[i] = psum[i - 1] + nums[i - 1]
        result = 0
        for i in range(1, n):
            l = psum[i] - psum[0]
            r = psum[n] - psum[i]
            if l >= r:
                result += 1
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
