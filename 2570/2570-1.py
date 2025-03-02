#! /usr/bin/env python

from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        pass


def main():
    examples = (
        (
            [[1, 2], [2, 3], [4, 5]], [[1, 4], [3, 2], [4, 1]], [[1, 6], [2, 3], [3, 2], [4, 6]]
        ),
        (
            [[2, 4], [3, 6], [5, 5]], [[1, 3], [4, 3]], [[1, 3], [2, 4], [3, 6], [4, 3], [5, 5]]
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums1, nums2, expected = example
        got = solution.mergeArrays(
            nums1=nums1,
            nums2=nums2
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
