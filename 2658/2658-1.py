#! /usr/bin/python python python3

from typing import List


class Solution:
    def findMaxFish(self,  grid: List[List[int]]) -> int:
        pass


def main():
    examples = (
        (
            [[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]], 7
        ),
        (
            [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]], 1
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        grid, expected = example
        got = solution.findMaxFish(
            grid=grid,
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
