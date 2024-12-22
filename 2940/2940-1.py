#! /usr/bin/python python

from typing import List


class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(heights)
        possibility = [0] * n
        stack = []
        for i, height in enumerate(heights):
            while stack and stack[-1][0] < height:
                _, j = stack.pop()
                possibility[j] = i
            stack.append((height, i))
        while stack:
            possibility[stack[-1][1]] = -1
            stack.pop()
        result = []
        for alice, bob in queries:
            left = min(alice, bob)
            right = max(alice, bob)
            if left == right or heights[left] < heights[right]:
                result.append(right)
            else:
                if possibility[right] == -1 or possibility[left] == -1:
                    result.append(-1)
                elif heights[possibility[right]] > heights[left]:
                    result.append(possibility[right])
                elif possibility[left] > right:
                    result.append(possibility[left])
                else:
                    i = possibility[right]
                    f = max(heights[left], heights[right])
                    while i < n and heights[i] <= f:
                        i += 1
                    if i == n:
                        result.append(-1)
                    else:
                        result.append(i)
        return result
        # n = len(heights)
        # possible = {}
        # for i in range(n):
        #     possible[i] = {i}
        #     for j in range(i + 1, n):
        #         if heights[j] > heights[i]:
        #             possible[i].add(j)
        # result = []
        # for query in queries:
        #     a, b = query
        #     intersection = possible[a].intersection(possible[b])
        #     if intersection:
        #         result.append(min(intersection))
        #     else:
        #         result.append(-1)
        # return result


def main():
    examples = (
        # (
        #     [6, 4, 8, 5, 2, 7], [[0, 1], [0, 3], [2, 4], [3, 4], [2, 2]], [2, 5, -1, 5, 2]
        # ),
        # (
        #     [5, 3, 8, 2, 6, 1, 4, 6], [[0, 7], [3, 5], [5, 2], [3, 0], [1, 6]], [7, 6, -1, 4, 6]
        # ),
        # (
        #     [1, 2, 1, 2, 1, 2], [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5]], [0, 1, 3, 3, 5, 5, 1, 1, -1, -1, -1, -1, 3, -1, 2, 3, 5, 5, 3, -1, 3, 3, -1, -1, 5, -1, 5, -1, 4, 5, 5, -1, 5, -1, 5, 5]
        # ),
        (
            [50000, 50002, 1, 2, 3, 49997, 50001], [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6]], [0, 1, 6, 6, 6, 6, 6]
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        heights, queries, expected = example
        got = solution.leftmostBuildingQueries(
            heights=heights,
            queries=queries
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
