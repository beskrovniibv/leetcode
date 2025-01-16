#! /usr/bin/python python python3

from typing import List


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        pass


def main():
    examples = (
        (
            [2, 1, 3], [10, 2, 5, 0], 13
        ),
        (
            [1, 2], [3, 4], 0
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums1, nums2, expected = example
        got = solution.xorAllNums(
            nums1=nums1,
            nums2=nums2
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
