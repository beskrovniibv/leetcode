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


def check(number):
    def check_(number, sq, _break, d):
        if _break:
            return True
        return check_(number, )
        pass
    return check_(number, number**2, False, 10)
    pass


if __name__ == "__main__":
    pre = [False]*1000
    for i in range(1001):
        pre[i] = check(i)
    main()
