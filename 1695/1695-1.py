#! /usr/bin/env python

from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        l, r = 0, 0
        d = {}
        s = 0
        while r < n:
            v = nums[r]
            if d.get(v, 0) != 0:
                while d.get(v) > 0:
                    v0 = nums[l]
                    s -= v0
                    d[v0] -= 1
                    l += 1
            r += 1
            d[v] = d.get(v, 0) + 1
            s += v
            result = max(result, s)
        return result


def main():
    examples = (
        (
            [4, 2, 4, 5, 6], 17
        ),
        (
            [5, 2, 1, 2, 5, 2, 1, 2, 5], 8
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, expected = example
        got = solution.maximumUniqueSubarray(
            nums=nums,
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
