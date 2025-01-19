#! /usr/bin/python python python3

from heapq import heappop, heappush
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        row_num, col_num = len(heightMap), len(heightMap[0])
        visited = [[False] * col_num for _ in range(row_num)]
        heap = []
        for row in range(row_num):
            for col in range(col_num):
                if row == 0 or row == row_num - 1 or col == 0 or col == col_num - 1:
                    heappush(heap, (heightMap[row][col], row, col))
                    visited[row][col] = True
        result = 0
        dirs = ((-1, 0), (+1, 0), (0, -1), (0, +1))
        while heap:
            h, row, col = heappop(heap)
            for dx, dy in dirs:
                new_row = row + dy
                new_col = col + dx
                if 0 <= new_row < row_num and 0 <= new_col < col_num and not visited[new_row][new_col]:
                    result += max(0, h - heightMap[new_row][new_col])
                    visited[new_row][new_col] = True
                    heappush(heap, (max(h, heightMap[new_row][new_col]), new_row, new_col))
        return result


def main():
    examples = (
        (
            [[5, 5, 5, 1], [5, 1, 1, 5], [5, 1, 5, 5], [5, 2, 5, 8]], 3
        ),
        (
            [[12, 13, 1, 12], [13, 4, 13, 12], [13, 8, 10, 12], [12, 13, 12, 12], [13, 13, 13, 13]], 14
        ),
        (
            [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]], 4
        ),
        (
            [[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]], 10
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        heightMap, expected = example
        got = solution.trapRainWater(
            heightMap=heightMap
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
