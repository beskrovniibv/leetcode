#! /usr/bin/python python python3

from collections import deque
from typing import List


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        mx = m*n + 1
        ans = [[mx]*(m) for _ in range(n)]
        ans[0][0] = 0
        # строка, столбец
        neibourghs = ((0, +1, 1), (0, -1, 2), (+1, 0, 3), (-1, 0, 4))
        queue = deque([(0, 0)])
        while queue:
            row, col = queue.popleft()
            for dx, dy, direction in neibourghs:
                _row = row + dx
                _col = col + dy
                cost = 0 if grid[row][col] == direction else 1
                if (_row >= 0 and _row < n and _col >= 0 and _col < m) and (ans[row][col] + cost < ans[_row][_col]):
                    ans[_row][_col] = ans[row][col] + cost
                    if cost == 1:
                        queue.append((_row, _col))
                    else:
                        queue.appendleft((_row, _col))
        return ans[n - 1][m - 1]


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
