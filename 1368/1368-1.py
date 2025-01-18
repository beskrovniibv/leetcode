#! /usr/bin/python python python3

from typing import List


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        pass


def main():
    examples = (
        (
            [[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]], 3
        ),
        (
            [[1, 1, 3], [3, 2, 2], [1, 1, 4]], 0
        ),
        (
            [[1, 2], [4, 3]], 1
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        grid, expected = example
        got = solution.minCost(
            grid=grid
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
