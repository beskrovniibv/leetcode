#! usr/bin/python

# 1578. Minimum Time to Make Rope Colorful

from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        result = 0
        i = 0
        p = None
        while i < len(colors):
            if p:
                if colors[i] == p:
                    result += min(neededTime[i], neededTime[i - 1])
                    neededTime[i] = max(neededTime[i], neededTime[i - 1])
            p = colors[i]
            i += 1
        return result


if __name__ == '__main__':
    # case 1
    colors = "abaac"
    neededTime = [1, 2, 3, 4, 5]

    solution = Solution()
    answer = solution.minCost(colors, neededTime)
    print(answer)
