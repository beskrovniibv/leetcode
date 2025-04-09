#! /usr/bin/env python

from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        result = 0
        v = set()
        for num in nums:
            if num < k:
                return -1
            if num > k:
                if num not in v:
                    result += 1
                    v.add(num)
        return result


def main():
    examples = (
        (
            [5, 2, 5, 4, 5], 2, 2
        ),
        (
            [2, 1, 2], 2, -1
        ),
        (
            [9, 7, 5, 3], 1, 4
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, k, expected = example
        got = solution.minOperations(
            nums=nums,
            k=k
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
