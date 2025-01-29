#! /usr/bin/python python python3

from collections import deque
from typing import List


class Solution:
    def findMaxFish(self,  grid: List[List[int]]) -> int:
        result = 0
        row_num, col_num = len(grid), len(grid[0])
        visited = [[False]*col_num for _ in range(row_num)]
        dirs = ((0, +1), (0, -1), (+1, 0), (-1, 0))
        for row in range(row_num):
            for col in range(col_num):
                if grid[row][col] != 0 and not visited[row][col]:
                    q = deque([(row, col)])
                    t = 0
                    while q:
                        r, c = q.popleft()
                        if visited[r][c]:
                            continue
                        visited[r][c] = True
                        t += grid[r][c]
                        for (dr, dc) in dirs:
                            nr = r + dr
                            nc = c + dc
                            if nr >= 0 and nr < row_num and nc >= 0 and nc < col_num and grid[nr][nc] != 0:
                                q.append((nr, nc))
                    result = max(result, t)
        return result


def main():
    examples = (
        (
            [[8, 6], [2, 6]], 22
        ),
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
