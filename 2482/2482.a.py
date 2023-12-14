#! usr/bin.python

# 2482. Difference Between Ones and Zeros in Row and Column

from typing import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        result = [[0] * n for _ in range(m)]
        zcount_r = [0] * m
        ocount_r = [0] * m
        zcount_c = [0] * n
        ocount_c = [0] * n
        for i in range(m):
            for j in range(n):
                zcount_r[i] += 1 if grid[i][j] == 0 else 0
                ocount_r[i] += 1 if grid[i][j] == 1 else 0
                zcount_c[j] += 1 if grid[i][j] == 0 else 0
                ocount_c[j] += 1 if grid[i][j] == 1 else 0
        for i in range(m):
            for j in range(n):
                result[i][j] = ocount_r[i] + ocount_c[j] - zcount_r[i] - zcount_c[j]
        return result


if __name__ == '__main__':
    # case 1
    grid = [[0, 1, 1], [1, 0, 1], [0, 0, 1]]

    solution = Solution()
    answer = solution.onesMinusZeros(grid)
    print(*answer)
