#! /usr/bin/python python python3

import collections
from functools import lru_cache
from typing import List


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MODULO = 1_000_000_007
        n = len(words[0])
        counts = [dict() for _ in range(n)]
        for i in range(n):
            for word in words:
                counts[i][word[i]] = counts[i].get(word[i], 0) + 1

        @lru_cache(maxsize=None)
        def dp(i, j):
            if i == len(target):
                return 1
            if j == n:
                return 0
            return (dp(i + 1, j + 1)*counts[j].get(target[i], 0) + dp(i, j + 1)) % MODULO

        return dp(0, 0)


def main():
    examples = (
        (
            ["acca", "bbbb", "caca"], "aba",  6
        ),
        (
            ["abba", "baab"], "bab", 4
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        words, target, expected = example
        got = solution.numWays(
            words=words,
            target=target
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
