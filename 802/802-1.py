#! /usr/bin/python python python3

from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        pass


def main():
    examples = (
        (
            [[1, 2], [2, 3], [5], [0], [5], [], []], [2, 4, 5, 6]
        ),
        (
            [[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []], [4]
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        graph, expected = example
        got = solution.eventualSafeNodes(
            graph=graph
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
