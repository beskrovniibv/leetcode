#! /usr/bin/python python python3

from collections import deque
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        queue = deque()
        row_num, col_num = len(isWater), len(isWater[0])
        result = [[-1]*col_num for _ in range(row_num)]
        for row in range(row_num):
            for col in range(col_num):
                if isWater[row][col] == 1:
                    queue.append((row, col, 0))
        dirs = ((-1, 0), (0, -1), (+1, 0), (0, +1))
        while queue:
            row, col, value = queue.popleft()
            if value == 0:
                result[row][col] = 0
            for dx, dy in dirs:
                new_row, new_col = row + dy, col + dx
                if new_row >= 0 and new_row < row_num and new_col >= 0 and new_col < col_num:
                    if isWater[new_row][new_col] == 1:
                        continue
                    if result[new_row][new_col] == -1 or result[new_row][new_col] > value + 1:
                        result[new_row][new_col] = value + 1
                        queue.append((new_row, new_col, value + 1))
        return result


def main():
    examples = (
        (
            [[0, 1], [0, 0]], [[1, 0], [2, 1]]
        ),
        (
            [[0, 0, 1], [1, 0, 0], [0, 0, 0]], [[1, 1, 0], [0, 1, 1], [1, 2, 2]]
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        isWater, expected = example
        got = solution.highestPeak(
            isWater=isWater
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
