#! usr/bin/python

# 661. Image Smoother

from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row_count = len(img)
        col_count = len(img[0])
        result = [[0] * col_count for _ in range(row_count)]
        for row in range(row_count):
            for col in range(col_count):
                sum, cnt = 0, 0
                for r in range(row - 1, row + 2):
                    for c in range(col - 1, col + 2):
                        if r < 0 or r >= row_count or c < 0 or c >= col_count:
                            continue
                        sum += img[r][c]
                        cnt += 1
                # c = 1
                # s = img[row][col]
                # if row == 0 and col == 0:
                #     # TL
                #     c += 3
                #     s += (
                #         img[row][col + 1]
                #         + img[row + 1][col]
                #         + img[row + 1][col + 1])
                # elif row == 0 and col == col_count - 1:
                #     # TR
                #     c += 3
                #     s += (
                #         img[row][col - 1]
                #         + img[row + 1][col]
                #         + img[row + 1][col - 1])
                # elif row == row_count - 1 and col == 0:
                #     # BL
                #     c += 3
                #     s += (
                #         img[row][col + 1]
                #         + img[row - 1][col]
                #         + img[row - 1][col + 1])
                # elif row == row_count - 1 and col == col_count - 1:
                #     # BR
                #     c += 3
                #     s += (
                #         img[row][col - 1]
                #         + img[row - 1][col]
                #         + img[row - 1][col - 1])
                # elif row == 0:
                #     # T
                #     c += 5
                #     s += (
                #         img[row][col - 1]
                #         + img[row][col + 1]
                #         + img[row + 1][col - 1]
                #         + img[row + 1][col]
                #         + img[row + 1][col + 1]
                #     )
                # elif row == row_count - 1:
                #     # B
                #     c += 5
                #     s += (
                #         img[row][col - 1]
                #         + img[row][col + 1]
                #         + img[row - 1][col - 1]
                #         + img[row - 1][col]
                #         + img[row - 1][col + 1]
                #     )
                # elif col == 0:
                #     # L
                #     c += 5
                #     s += (
                #         img[row - 1][col]
                #         + img[row - 1][col + 1]
                #         + img[row][col + 1]
                #         + img[row + 1][col]
                #         + img[row + 1][col + 1]
                #     )
                # elif col == col_count - 1:
                #     # R
                #     c += 5
                #     s += (
                #         img[row - 1][col]
                #         + img[row - 1][col - 1]
                #         + img[row][col - 1]
                #         + img[row + 1][col]
                #         + img[row + 1][col - 1]
                #     )
                # else:
                #     # other
                #     c += 8
                #     s += (
                #         img[row - 1][col - 1]
                #         + img[row - 1][col]
                #         + img[row - 1][col + 1]
                #         + img[row][col - 1]
                #         + img[row][col + 1]
                #         + img[row + 1][col - 1]
                #         + img[row + 1][col]
                #         + img[row + 1][col + 1]
                #     )
                result[row][col] = sum // cnt
        return result


if __name__ == '__main__':
    # case 1
    # img = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    # case 2
    # img = [[100, 200, 100], [200, 50, 200], [100, 200, 100]]
    # case 3
    img = [[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13], [14, 15, 16]]

    solution = Solution()
    answer = solution.imageSmoother(img)
    print(*answer)
