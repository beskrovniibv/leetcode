#! /usr/bin/env python

from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        c = {}
        e = {}
        i = 0
        for (_from, _to) in edges:
            c1 = e.get(_from)
            c2 = e.get(_to)
            if c1 and c2 and c1 == c2:
                return [_from, _to]
            elif c1 and c2:
                for j in c[c2]:
                    e[j] = c1
                c[c1] = c[c1].union(c[c2])
                c[c2] = None
            elif not (c1 or c2):
                e[_from] = i + 1
                e[_to] = i + 1
                i += 1
                c[i] = {_from, _to}
            elif not c2:
                e[_to] = e[_from]
                c[c1].add(_to)
            elif not c1:
                e[_from] = e[_to]
                c[c2].add(_from)


def main():
    examples = (
        (
            [[1, 2], [3, 4], [2, 3], [1, 4], [1, 5]], [1, 4]
        ),
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
