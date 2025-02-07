#! /usr/bin/env python

from typing import List


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        n = len(queries)
        result = [0]*n
        balls = {}
        colors = {}
        i = 0
        for x, y in queries:
            prev = i > 0 and result[i - 1] or 0
            color = balls.get(x)
            if color:
                colors[color] -= 1
                if not colors[color]:
                    prev = prev - 1
            balls[x] = y
            colors[y] = colors.get(y, 0) + 1
            result[i] = prev + (1 if colors[y] == 1 else 0)
            i += 1
        return result


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
