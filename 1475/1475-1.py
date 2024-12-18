#! /usr/bin/python python

from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        pass


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
