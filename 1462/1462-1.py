#! /usr/bin/python python python3

from collections import deque
from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        routes = [set() for _ in range(numCourses)]
        n = len(queries)
        result = [False]*n
        d = {}
        for pair in prerequisites:
            d[pair[1]] = d.get(pair[1], [])
            d[pair[1]].append(pair[0])
        for i in range(numCourses):
            q = deque([i])
            visited = set()
            while q:
                prev = q.popleft()
                for prev in d.get(prev, []):
                    if prev in visited:
                        continue
                    routes[i].add(prev)
                    q.append(prev)
                    visited.add(prev)
        for i, (f, t) in enumerate(queries):
            result[i] = f in routes[t]
        return result


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
        (
            5, [[0, 1], [1, 2], [2, 3], [3, 4]], [[0, 4], [4, 0], [1, 3], [3, 0]], [True, False, True, False]
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
