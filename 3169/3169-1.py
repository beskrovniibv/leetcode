#! /usr/bin/env python

from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        result = 0
        last = 0
        for b, e in sorted(meetings):
            if b > last + 1:
                result += b - last - 1
            last = max(e, last)
        result += days - last
        return result


def main():
    examples = (
        (
            10, [[5, 7], [1, 3], [9, 10]], 2
        ),
        (
            5, [[2, 4], [1, 3]], 1
        ),
        (
            6, [[1, 6]], 0
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        days, meetings, expected = example
        got = solution.countDays(
            days=days,
            meetings=meetings
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
