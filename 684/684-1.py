#! /usr/bin/env python

from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        pass


def main():
    examples = (
        (
            [[1, 2], [1, 3], [2, 3]], [2, 3]
        ),
        (
            [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]], [1, 4]
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        edges, expected = example
        got = solution.findRedundantConnection(
            edges=edges
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
