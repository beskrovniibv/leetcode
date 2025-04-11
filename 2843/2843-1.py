#! /usr/bin/env python


class Solution:
    def digits_sum(self, value: int) -> int:
        result = 0
        while value > 0:
            result += value % 10
            value //= 10
        return result

    def symmetric(self, value: int) -> bool:
        if value < 10:
            radix = 1
        elif value < 100:
            radix = 2
        elif value < 1_000:
            radix = 3
        elif value < 10_000:
            radix = 4
        elif value < 100_000:
            radix = 5
        elif value < 1_000_000:
            radix = 6
        if radix & 1 == 1:
            return False
        div = 10**(radix//2)
        left, right = value//div, value % div
        return self.digits_sum(left) == self.digits_sum(right)

    def countSymmetricIntegers(self, low: int, high: int) -> int:
        result = 0
        for i in range(low, high + 1):
            if self.symmetric(i):
                result += 1
        return result


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
