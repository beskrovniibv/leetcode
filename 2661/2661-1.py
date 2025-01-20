#! /usr/bin/python python python3

from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        num, row_num, col_num = len(arr), len(mat), len(mat[0])
        rows, cols = [0]*row_num, [0]*col_num
        cells = {}
        for row in range(row_num):
            for col in range(col_num):
                cells[mat[row][col]] = (row, col)
        for i in range(num):
            r, c = cells[arr[i]]
            rows[r] += 1
            cols[c] += 1
            if rows[r] == col_num or cols[c] == row_num:
                return i


def main():
    examples = (
        (
            [1, 4, 5, 2, 6, 3], [[4, 3, 5], [1, 2, 6]], 1
        ),
        (
            [1, 3, 4, 2], [[1, 4], [2, 3]], 2
        ),
        (
            [2, 8, 7, 4, 1, 3, 5, 6, 9], [[3, 2, 5], [1, 4, 6], [8, 7, 9]], 3
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        arr, mat, expected = example
        got = solution.firstCompleteIndex(
            arr=arr,
            mat=mat,
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
