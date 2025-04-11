#! /usr/bin/env python


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        pass


def main():
    examples = (
        (
            1, 100, 9
        ),
        (
            1200, 1230, 4
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        low, high, expected = example
        got = solution.countSymmetricIntegers(
            low=low,
            high=high
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
