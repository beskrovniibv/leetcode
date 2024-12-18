#! /usr/bin/python python

from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        discounts = [0] * n
        stack = []
        for i, price in enumerate(prices):
            while stack and stack[-1][0] >= price:
                _, j = stack.pop()
                discounts[j] = i
            stack.append((price, i))
        while stack:
            _, j = stack.pop()
            discounts[j] = -1
        return [price - (prices[discount] if discount >= 0 else 0) for price, discount in zip(prices, discounts)]


def main():
    examples = (
        (
            [8, 4, 6, 2, 3],  [4, 2, 4, 2, 3]
        ),
        (
            [1, 2, 3, 4, 5],  [1, 2, 3, 4, 5]
        ),
        (
            [10, 1, 1, 6],  [9, 0, 1, 6]
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        prices, expected = example
        got = solution.finalPrices(
            prices=prices
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
