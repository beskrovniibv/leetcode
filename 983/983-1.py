#! /usr/bin/python python python3

from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = days[-1]
        dp = [0] * (n + 1)
        i = 0
        for day in range(1, n + 1):
            if day < days[i]:
                dp[day] = dp[day - 1]
            else:
                i += 1
                dp[day] = min(
                    dp[day - 1] + costs[0],
                    dp[max(0, day - 7)] + costs[1],
                    dp[max(0, day - 30)] + costs[2],
                )
        return dp[n]


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
