#! /usr/bin/python python python3

from typing import List


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        used = [0]*n
        parents = [None]*n
        mxc = 0

        def dfs(v):
            global mxc
            used[v] = 1
            for to in favorite:
                if not used[to]:
                    dfs(to)
                    parents[to] = v
                elif used[to] == 1:
                    cycle = []
                    while parents[v] != to:
                        cycle.append(v)
                        v = parents[v]
                    cycle.append(to)
                    mxc = max(mxc, len(cycle))
                used[v] = 2

        reversed = [[] for _ in range(n)]
        for i in range(n):
            reversed[favorite[i]].append(i)
        dfs(0)
        print(mxc)
        print(reversed)



def main():
    examples = (
        (
            [2, 2, 1, 2], 3
        ),
        (
            [1, 2, 0], 3
        ),
        (
            [3, 0, 1, 4, 1], 4
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        favorite, expected = example
        got = solution.maximumInvitations(
            favorite=favorite
        )
        assert got == expected, f"Error in sample {idx+ 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
