#! usre/bin/python

# 2706. Buy Two Chocolates

from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        result = money
        prices.sort()
        if money >= prices[0] + prices[1]:
            result = money - ( prices[0] + prices[1])
        return result


if __name__ == '__main__':
    # case 1
    prices = [1, 2, 2]
    money = 3
    # case 2
    # prices = [3, 2, 3]
    # money = 3

    solution = Solution()
    answer = solution.buyChoco(prices, money)
    print(answer)
