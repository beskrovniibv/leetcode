#! /usr/bin/env python

MODULO = 10**9 + 7


class Solution:
    def countGoodNumbers(self, n: int) -> int:
        pass


def main():
    examples = (
        (
            1, 5
        ),
        (
            4, 400
        ),
        (
            50, 564908303
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        n, expected = example
        got = solution.countGoodNumbers(
            n=n
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
