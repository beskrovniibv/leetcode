#! /usr/bin/env python

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        pass


def main():
    examples = (
        (
            "daabcbaabcbc", "abc", "dab"
        ),
        (
            "axxxxyyyyb", "xy", "ab"
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        s, part, expected = example
        got = solution.removeOccurrences(
            s=s,
            part=part
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
