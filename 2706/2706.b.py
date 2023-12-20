#! usre/bin/python

# 2706. Buy Two Chocolates

from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        mn1, mn2 = None, None
        for price in prices:
            if not mn1:
                mn1 = price
            elif not mn2:
                if price < mn1:
                    mn2 = mn1
                    mn1 = price
                else:
                    mn2 = price
            elif price < mn1:
                mn2 = mn1
                mn1 = price
            elif price < mn2:
                mn2 = price
        return money if money < mn1 + mn2 else (money - mn1 - mn2)


if __name__ == '__main__':
    # case 1
    # prices = [1, 2, 2]
    # money = 3
    # case 2
    prices = [3, 2, 3]
    money = 3

    solution = Solution()
    answer = solution.buyChoco(prices, money)
    print(answer)
