#! /usr/bin/env python

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        pass


def main():
    examples = (
        (
            "aeioqq", 1, 0
        ),
        (
            "aeiou", 0, 1
        ),
        (
            "ieaouqqieaouqq", 1, 3
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        word, k, expected = example
        got = solution.countOfSubstrings(
            word=word,
            k=k
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
