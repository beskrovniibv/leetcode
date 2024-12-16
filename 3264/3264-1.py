#! /usr/bin/python python

from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        indexed = [[num, i] for i, num in enumerate(nums)]
        heapify(indexed)
        for _ in range(k):
            num, i = heappop(indexed)
            nums[i] *= multiplier
            heappush(indexed, [num*multiplier, i])
        return nums


def main():
    examples = (
        (
            [2, 1, 3, 5, 6], 5, 2,  [8, 4, 6, 5, 6]
        ),
        (
            [1, 2], 3, 4,  [16, 8]
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, k, multiplier, expected = example
        got = solution.getFinalState(
            nums=nums,
            k=k,
            multiplier=multiplier
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
