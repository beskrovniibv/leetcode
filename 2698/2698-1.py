#! /usr/bin/env python

class Solution:
    def punishmentNumber(self, n: int) -> int:
        pass


def main():
    examples = (
        (
            10, 182
        ),
        (
            37, 1478
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        n, expected = example
        got = solution.punishmentNumber(
            n=n
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
