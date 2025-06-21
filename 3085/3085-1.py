#! /usr/bin/env python

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        pass


def main():
    examples = (
        (
            "aabcaba", 0, 3
        ),
        (
            "dabdcbdcdcd", 2, 2
        ),
        (
            "aaabaaa", 2, 1
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        word, k, expected = example
        got = solution.minimumDeletions(
            word=word,
            k=k,
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expeted}, got {got}"


if __name__ == "__main__":
    main()
