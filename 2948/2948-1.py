#! /usr/bin/python python python3

from typing import List


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        pass


def main():
    examples = (
        (
            [1, 5, 3, 9, 8], 2, [1, 3, 5, 8, 9]
        ),
        (
            [1, 7, 6, 18, 2, 1], 3, [1, 6, 7, 18, 1, 2]
        ),
        (
            [1, 7, 28, 19, 10], 3, [1, 7, 28, 19, 10]
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, limit, expected = example
        got = solution.lexicographicallySmallestArray(
            nums=nums,
            limit=limit
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
