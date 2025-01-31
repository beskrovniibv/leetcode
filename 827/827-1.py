#! /usr/bin/env python

from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        pass


def main():
    examples = (
        (
            [[1, 0], [0, 1]], 3
        ),
        (
            [[1, 1], [1, 0]], 4
        ),
        (
            [[1, 1], [1, 1]], 4
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        grid, expected = example
        got = solution.largestIsland(
            grid=grid
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
