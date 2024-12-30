#! /usr/bin/python python pyton3

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        pass


def main():
    examples = (
        (
            3, 3, 1, 1, 8
        ),
        (
            2, 3, 1, 2, 5
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        low, high, zero, one, expected = example
        got = solution.countGoodStrings(
            low=low,
            high=high,
            zero=zero,
            one=one
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
