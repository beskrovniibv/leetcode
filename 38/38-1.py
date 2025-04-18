#! /usr/bin/env python

class Solution:
    def countAndSay(self, n: int) -> str:
        pass


def main():
    examples = (
        (
            4, "1211"
        ),
        (
            1, "1"
        )
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        n, expected = example
        got = solution.countAndSay(
            n=1
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
