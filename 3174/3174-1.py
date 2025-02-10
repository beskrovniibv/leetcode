#! /usr/bin/env python

class Solution:
    def clearDigits(self, s: str) -> str:
        pass


def main():
    examples = (
        (
            "abc", "abc"
        ),
        (
            "cb34", ""
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        s, expected = example
        got = solution.clearDigits(
            s=s
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
