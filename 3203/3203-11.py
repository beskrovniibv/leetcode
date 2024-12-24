#! /usr/bin/python python

from typing import List


class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        pass


def main():
    examples = (
        (
            [[0, 1], [0, 2], [0, 3]], [[0, 1]], 3
        ),
        (
            [[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]], [[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]], 5
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        edges1, edges2, expected = example
        got = solution.minimumDiameterAfterMerge(
            edges1=edges1,
            edges2=edges2
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
