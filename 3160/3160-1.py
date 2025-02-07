#! /usr/bin/env python

from typing import List


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        pass


def main():
    examples = (
        (
            4, [[1, 4], [2, 5], [1, 3], [3, 4]], [1, 2, 2, 3]
        ),
        (
            4, [[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]], [1, 2, 2, 3, 4]
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        limit, queries, expected = example
        got = solution.queryResults(
            limit=limit,
            queries=queries
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
