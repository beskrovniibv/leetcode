#! /usr/bin/python python

from typing import List


class Solution:
    def dfs(self, v, graph, visited, dia=[0]):
        visited.add(v)
        md1, md2 = 0, 0
        for n in graph[v]:
            if n not in visited:
                d = self.dfs(n, graph, visited, dia)
                if d > md1:
                    md2 = md1
                    md1 = d
                elif d > md2:
                    md2 = d
        dia[0] = max(dia[0], md1 + md2)
        return md1 + 1

    def get_diameter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        visited = set()
        leaves = set()
        for u, v in edges:
            if u not in visited:
                visited.add(u)
                leaves.add(u)
            if v not in visited:
                visited.add(v)
                leaves.add(v)
            graph[u].append(v)
            graph[v].append(u)
            if len(graph[u]) > 1:
                leaves.discard(u)
            if len(graph[v]) > 1:
                leaves.discard(v)
        visited = set()
        if not leaves:
            return 0
        dia = [0]
        self.dfs(leaves.pop(), graph, visited, dia)
        return dia[0]

    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        d1 = self.get_diameter(edges1)
        d2 = self.get_diameter(edges2)
        d12 = (d1 + 1)//2 + (d2 + 1)//2 + 1
        return max(d1, d2, d12)


def main():
    examples = (
        (
            [[0, 1], [0, 2], [0, 3]], [[0, 1]], 3
        ),
        (
            [[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]], [[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]], 5
        ),
        (
            [], [], 1
        ),
        (
            [[3, 0], [2, 1], [2, 3]], [[0, 1], [0, 4], [3, 5], [6, 3], [7, 6], [2, 7], [0, 2], [8, 0], [8, 9]], 7
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
