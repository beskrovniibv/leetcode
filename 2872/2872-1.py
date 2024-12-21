from typing import List


class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        if n == 1:
            return 1
        tree = {}
        result = 0

        def dfs(vertex, parent):
            nonlocal result
            subtreesum = values[vertex]
            for v in tree[vertex]:
                if v != parent:
                    subtreesum += dfs(v, vertex)
            if subtreesum % k == 0:
                result += 1
            return subtreesum

        for edge in edges:
            p1, p2 = edge
            tree[p1] = tree.get(p1, [])
            tree[p1].append(p2)
            tree[p2] = tree.get(p2, [])
            tree[p2].append(p1)

        dfs(0, -1)

        return result


def main():
    examples = (
        (
            5, [[0, 2], [1, 2], [1, 3], [2, 4]], [1, 8, 1, 4, 4], 6, 2
        ),
        (
            7, [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]], [3, 0, 6, 1, 5, 2, 1], 3, 3
        ),
        (
            1, [], [0], 1, 1
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        n, edges, values, k, expected = example
        got = solution.maxKDivisibleComponents(
            n=n,
            edges=edges,
            values=values,
            k=k
        )
        assert expected == got, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
