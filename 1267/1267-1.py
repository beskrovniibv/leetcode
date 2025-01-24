#! /usr/bin/python python python3

from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row_num, col_num = len(grid), len(grid[0])
        rows, cols = {}, {}
        for row in range(row_num):
            for col in range(col_num):
                if grid[row][col] == 1:
                    rows[row] = rows.get(row, [])
                    rows[row].append((row, col))
                    cols[col] = cols.get(col, [])
                    cols[col].append((row, col))
        result = set()
        for row in rows:
            if len(rows[row]) > 1:
                for srv in rows[row]:
                    result.add(srv)
        for col in cols:
            if len(cols[col]) > 1:
                for srv in cols[col]:
                    result.add(srv)
        return len(result)


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
