#! /usr/bin/env python

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        pass


def main():
    examples = (
        (
            "IIIDIDDD", "123549876"
        ),
        (
            "DDD", "4321"
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        pattern, expected = example
        got = solution.smallestNumber(
            pattern=pattern
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
