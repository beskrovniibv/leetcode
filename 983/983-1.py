#! /usr/bin/python python python3

from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        pass


def main():
    examples = (
        (
            [1, 4, 6, 7, 8, 20], [2, 7, 15], 11
        ),
        (
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15], 17
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        days, costs, expected = example
        got = solution.mincostTickets(
            days=days,
            costs=costs
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
