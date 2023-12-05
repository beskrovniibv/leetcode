#! usr/bin/python

# 1266. Minimum Time Visiting All Points

from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        result = 0
        if len(points) == 1:
            return 0
        start = points[0]
        i = 1
        while i < len(points):
            next = points[i]
            x1, y1 = start[0], start[1]
            x2, y2 = next[0], next[1]
            while x2 != x1 or y2 != y1:
                if x2 > x1:
                    dx = 1
                elif x2 < x1:
                    dx = -1
                elif x2 == x1:
                    dx = 0
                else:
                    assert 'smth was going wrong'
                if y2 > y1:
                    dy = 1
                elif y2 < y1:
                    dy = -1
                elif y2 == y1:
                    dy = 0
                else:
                    assert 'smth was going wrong'
                x1 += dx
                y1 += dy
                result += 1
            start = next
            i += 1
        return result


if __name__ == '__main__':
    # case 1
    points = [[1, 1], [3, 4], [-1, 0]]
    # case 2
    # points = [[3, 2], [-2, 2]]

    solution = Solution()
    answer = solution.minTimeToVisitAllPoints(points)
    print(answer)
