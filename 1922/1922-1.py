#! /usr/bin/env python

MODULO = 10**9 + 7


def pow(a: int, b: int) -> int:
    result = 1
    while b > 0:
        if b & 1 == 1:
            result *= a
            b -= 1
        a = a**2 % MODULO
        b = b // 2
    return result % MODULO


class Solution:
    def countGoodNumbers(self, n: int) -> int:
        return pow(5, (n + 1)//2)*pow(4, n//2) % MODULO


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
        (
            806166225460393, 643535977
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
