#! /usr/bin/python python python3

from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        row_num, col_num = len(heightMap), len(heightMap[0])
        l2r_mx = [[0]*col_num for _ in range(row_num)]
        r2l_mx = [[0]*col_num for _ in range(row_num)]
        u2d_mx = [[0]*col_num for _ in range(row_num)]
        d2u_mx = [[0]*col_num for _ in range(row_num)]
        for row in range(row_num):
            for col in range(col_num):
                if col == 0:
                    l2r_mx[row][col] = heightMap[row][col]
                else:
                    l2r_mx[row][col] = max(heightMap[row][col], l2r_mx[row][col - 1])
        for row in range(row_num):
            for col in range(col_num - 1, -1, -1):
                if col == col_num - 1:
                    r2l_mx[row][col] = heightMap[row][col]
                else:
                    r2l_mx[row][col] = max(heightMap[row][col], r2l_mx[row][col + 1])
        for col in range(col_num):
            for row in range(row_num):
                if row == 0:
                    u2d_mx[row][col] = heightMap[row][col]
                else:
                    u2d_mx[row][col] = max(heightMap[row][col], u2d_mx[row - 1][col])
        for col in range(col_num):
            for row in range(row_num - 1, -1, -1):
                if row == row_num - 1:
                    d2u_mx[row][col] = heightMap[row][col]
                else:
                    d2u_mx[row][col] = max(heightMap[row][col], d2u_mx[row + 1][col])
        # for row in heightMap:
        #     print(*row)
        # print()
        for row in l2r_mx:
            print(*row)
        print()
        for row in r2l_mx:
            print(*row)
        print()
        for row in u2d_mx:
            print(*row)
        print()
        for row in d2u_mx:
            print(*row)
        # [a, b, c, d] - a - слева; b - справа; c - сверху; d - снизу
        dirs = ((-1, 0), (+1, 0), (0, -1), (0, +1))
        constraints = [[[0 for _ in range(4)] for _ in range(col_num)] for _ in range(row_num)]
        for row in range(row_num):
            for col in range(col_num):
                for d, (dx, dy) in enumerate(dirs):
                    new_row = row + dy
                    new_col = col + dx
                    if new_col >= 0 and new_col < col_num and new_row >= 0 and new_row < row_num:
                        if d == 0:
                            constraint = l2r_mx[row][col]
                        elif d == 1:
                            constraint = r2l_mx[row][col]
                        elif d == 2:
                            constraint = u2d_mx[row][col]
                        elif d == 3:
                            constraint = d2u_mx[row][col]
                        constraints[row][col][d] = constraint
                    else:
                        constraints[row][col][d] = heightMap[row][col]
        for row in constraints:
            print(*row)
        result = 0
        for row in range(row_num):
            if row == 0 or row == row_num - 1:
                continue
            for col in range(col_num):
                if col == 0 or col == col_num - 1:
                    continue
                h = min(constraints[row][col]) - heightMap[row][col]
                result += h
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
