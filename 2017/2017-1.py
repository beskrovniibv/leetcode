#! /usr/bin/python python python3

from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        psum0 = [0] + [0]*n
        psum1 = [0] + [0]*n
        for i in range(n):
            psum0[i + 1] = psum0[i] + grid[0][i]
            psum1[i + 1] = psum1[i] + grid[1][i]
        result = int(10e9) + 1
        for i in range(1, n + 1):
            v1 = psum0[-1] - psum0[i]
            v2 = psum1[-1] - (psum1[-1] - psum1[i - 1])
            result = min(result, max(v1, v2))
        return result


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
        (
            [[5, 12, 14], [20, 7, 17]], 20
        )
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
