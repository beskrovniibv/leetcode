#! /usr/bin/env python

from typing import List


class Solution:
    def minOperations(self,  grid: List[List[int]],  x: int) -> int:
        pass


def main():
    examples = (
        (
            [[2, 4], [6, 8]], 2, 4
        ),
        (
            [[1, 5], [2, 3]], 1, 5
        ),
        (
            [[1, 2], [3, 4]], 2, -1
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        grid, x, expected = example
        got = solution.minOperations(
            grid=grid,
            x=x
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
