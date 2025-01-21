#! /usr/bin/python python python3

from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        pass


def main():
    examples = (
        (
            [[2, 5, 4], [1, 5, 1]], 4
        ),
        (
            [[3, 3, 1], [8, 5, 2]], 4
        ),
        (
            [[1, 3, 1, 15], [1, 3, 3, 1]], 7
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        grid, expected = example
        got = solution.gridGame(
            grid=grid
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
