#! usr/bin/python

# 118. Pascal's Triangle

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        result = [[1], [1, 1]]
        for i in range(2, numRows):
            row = [1]
            for j in range(len(result[i - 1]) - 1):
                row.append(result[i - 1][j] + result[i - 1][j + 1])
            row.append(1)
            result.append(row)
        return result


if __name__ == '__main__':
    solution = Solution()
    answer = solution.generate(5)
    print(answer)
