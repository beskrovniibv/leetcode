#! /usr/bin/python python python3

from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vovels = "aeiou"
        n = len(words)
        psum = [0] + [0]*n
        for i in range(1, n + 1):
            word = words[i - 1]
            good = word[0] in vovels and word[-1] in vovels
            psum[i] = psum[i - 1] + (1 if good else 0)
        result = []
        for query in queries:
            b, e = query
            result.append(psum[e + 1] - psum[b])
        return result


def main():
    examples = (
        (
            ["aba", "bcb", "ece", "aa", "e"], [[0, 2], [1, 4], [1, 1]], [2, 3, 0]
        ),
        (
            ["a", "e", "i"], [[0, 2], [0, 1], [2, 2]], [3, 2, 1]
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        words, queries, expected = example
        got = solution.vowelStrings(
            words=words,
            queries=queries
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
