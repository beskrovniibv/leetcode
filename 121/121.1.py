#! usr/bin/python

# 121. Best Time to Buy and Sell Stock

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        minimum, profit = 10**4 + 1, -1
        for i in range(1, len(prices)):
            minimum = min(minimum, prices[i - 1])
            profit = max(profit, prices[i] - minimum)
            result = profit if profit > 0 else 0
        return result


if __name__ == '__main__':
    # case 1
    # prices = [7, 1, 5, 3, 6, 4]
    # case 2
    prices = [7, 6, 4, 3, 1]

    solution = Solution()
    answer = solution.maxProfit(prices)
    print(answer)
