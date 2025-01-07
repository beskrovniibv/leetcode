#! /usr/bin/python python python3

from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = set()
        for i, w1 in enumerate(words):
            for j, w2 in enumerate(words):
                if j == i:
                    continue
                if w2 in w1:
                    result.add(w2)
        return list(result)


def main():
    examples = (
        (
            ["mass", "as", "hero", "superhero"], ["hero", "as"]
        ),
        (
            ["leetcode", "et", "code"], ["code", "et", ]
        ),
        (
            ["blue", "green", "bu"], []
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        words, expected = example
        got = solution.stringMatching(
            words=words
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
