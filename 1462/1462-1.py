#! /usr/bin/python python python3

from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        pass


def main():
    examples = (
        (
            2, [[1, 0]], [[0, 1], [1, 0]], [False, True]
        ),
        (
            2, [], [[1, 0], [0, 1]], [False, False]
        ),
        (
            3, [[1, 2], [1, 0], [2, 0]], [[1, 0], [1, 2]], [True, True]
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        numCourses, prerequisites, queries, expected = example
        got = solution.checkIfPrerequisite(
            numCourses=numCourses,
            prerequisites=prerequisites,
            queries=queries
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
