#! /usr/bin/python python python3

from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        pass


def main():
    examples = (
        (
            ["mass", "as", "hero", "superhero"], ["as", "hero"]
        ),
        (
            ["leetcode", "et", "code"], ["et", "code"]
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
