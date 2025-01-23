#! /usr/bin/python python python3

from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        pass


def main():
    examples = (
        (
            [[1, 0], [0, 1]], 0
        ),
        (
            [[1, 0], [1, 1]], 3
        ),
        (
            [[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]], 4
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        grid, expected = example
        got = solution.countServers(
            grid=grid
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
