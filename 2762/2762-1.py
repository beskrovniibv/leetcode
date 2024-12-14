#! /usr/bin/python python

from typing import List


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        for ln in range(1, n + 1):
            for le in range(n - ln + 1):
                suba = nums[le:le + ln]
                mn = min(suba)
                mx = max(suba)
                result += 1 if mx - mn <= 2 else 0
        return result


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
