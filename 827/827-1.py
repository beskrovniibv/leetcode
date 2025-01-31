#! /usr/bin/env python

from collections import deque
from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        num_rows, num_cols = len(grid), len(grid[0])
        visited = [[False]*num_cols for _ in range(num_rows)]
        dirs = ((+1, 0), (-1, 0), (0, +1), (0, -1))
        cm = 1
        components = {}
        for row in range(num_rows):
            for col in range(num_cols):
                if visited[row][col] or grid[row][col] == 0:
                    continue
                s = 1
                visited[row][col] = True
                grid[row][col] = cm
                queue = deque([(row, col)])
                while queue:
                    r, c = queue.popleft()
                    grid[r][c] = cm
                    for (dy, dx) in dirs:
                        n_r = r + dy
                        n_c = c + dx
                        if n_r >= 0 and n_r < num_rows and n_c >= 0 and n_c < num_cols:
                            if visited[n_r][n_c]:
                                continue
                            if grid[n_r][n_c] != 0:
                                visited[n_r][n_c] = True
                                queue.append((n_r, n_c))
                                s += 1
                components[cm] = s
                if s == num_cols*num_rows:
                    return s
                cm += 1
        result = 0
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 0:
                    s = 1
                    p = set()
                    for (dy, dx) in dirs:
                        n_r, n_c = row + dy, col + dx
                        if n_r >= 0 and n_r < num_rows and n_c >= 0 and n_c < num_cols:
                            if grid[n_r][n_c] != 0 and grid[n_r][n_c] not in p:
                                s += components[grid[n_r][n_c]]
                                p.add(grid[n_r][n_c])
                    result = max(result, s)
        return result


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
