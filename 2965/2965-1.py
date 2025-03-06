#! /usr/bin/env python

from typing import List


class Solution:
    def findMissingAndRepeatedValues(self,  grid: List[List[int]]) -> List[int]:
        pass


def main():
    examples = (
        (
            [[1, 3], [2, 2]], [2, 4]
        ),
        (
            [[9, 1, 7], [8, 9, 2], [3, 4, 6]], [9, 5]
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        grid, expected = example
        got = solution.findMissingAndRepeatedValues(
            grid=grid
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
