#! usr/bin/python

# 1582. Special Positions in a Binary Matrix

from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        result = 0
        rows = len(mat)
        cols = len(mat[0])
        s_row = [0] * rows
        s_col = [0] * cols
        for r in range(rows):
            for c in range(cols):
                s_row[r] += mat[r][c]
                s_col[c] += mat[r][c]
        for i, r in enumerate(s_row):
            if r != 1:
                continue
            for j, c in enumerate(s_col):
                if c != 1:
                    continue
                if mat[i][j] == 1:
                    result += 1
        return result


if __name__ == '__main__':
    # case 1
    # nums = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]
    # case 35
    nums = [[0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0]]

    solution = Solution()
    answer = solution.numSpecial(nums)
    print(answer)
