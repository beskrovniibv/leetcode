#! /usr/bin/python python python3

from collections import deque
from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        indegree = [0] * n
        adj = [[] for _ in range(n)]

        for i in range(n):
            for node in graph[i]:
                adj[node].append(i)
                indegree[i] += 1

        q = deque()
        # Push all the nodes with indegree zero in the queue.
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        safe = [False] * n
        while q:
            node = q.popleft()
            safe[node] = True

            for neighbor in adj[node]:
                # Delete the edge "node -> neighbor".
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        safeNodes = []
        for i in range(n):
            if safe[i]:
                safeNodes.append(i)

        return safeNodes


def main():
    examples = (
        (
            [[], [0, 2, 3, 4], [3], [4], []], [0, 1, 2, 3, 4]
        ),
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
