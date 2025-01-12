#! /usr/bin/python python python3

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        pass


def main():
    examples = (
        (
            "))()))", "010100", True
        ),
        (
            "()()", "0000", True
        ),
        (
            ")", "0", False
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        s, locked, expected = example
        got = solution.canBeValid(
            s=s,
            locked=locked
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
