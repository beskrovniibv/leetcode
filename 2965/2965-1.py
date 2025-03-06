#! /usr/bin/env python

from typing import List


class Solution:
    def findMissingAndRepeatedValues(self,  grid: List[List[int]]) -> List[int]:
        n = 1
        s0 = 0
        s02 = 0
        s1 = 0
        s12 = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                s0 += n
                s1 += grid[i][j]
                s02 += n**2
                s12 += grid[i][j] ** 2
                n += 1

        v = ((s12 - s02)//(s1 - s0) + (s1 - s0)) // 2
        u = ((s12 - s02)//(s1 - s0) - (s1 - s0)) // 2
        return [v, u]


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
