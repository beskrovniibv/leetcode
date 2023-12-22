#! usr/bin/python

# 1637. Widest Vertical Area Between Two Points Containing No Points

from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda pos: pos[0])
        return max(points[i][0] - points[i - 1][0] for i in range(1, len(points)))


if __name__ == '__main__':
    # case 1
    # points = [[8, 7], [9, 9], [7, 4], [9, 7]]
    # case 2
    points = [[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]

    solution = Solution()
    answer = solution.maxWidthOfVerticalArea(points)
    print(answer)
