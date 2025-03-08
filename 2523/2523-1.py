#! /usr/bin/env python

from typing import List


def is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    if num & 1 == 0:
        return False
    d = 2
    while d*d <= num:
        if num % d == 0:
            return False
        d += 1
    return True


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        ans = [-1, -1]
        primes = []
        for num in range(left, right + 1):
            if is_prime(num):
                primes.append(num)
            if len(primes) >= 2:
                ans = [primes[0], primes[1]]
                best = ans[1] - ans[0]
                for i in range(1, len(primes)):
                    if primes[i] - primes[i - 1] <= 2:
                        return [primes[i - 1], primes[i]]
                    if primes[i] - primes[i - 1] < best:
                        best = primes[i] - primes[i - 1]
                        ans = [primes[i - 1], primes[i]]
        if len(primes) < 2:
            return [-1, -1]
        elif len(primes) == 2:
            return primes
        else:
            ans = [primes[0], primes[1]]
            best = ans[1] - ans[0]
            for i in range(1, len(primes) + 1):
                if primes[i] - primes[i - 1] <= 2:
                    return [primes[i - 1], primes[i]]
                if primes[i] - primes[i - 1] < best:
                    best = primes[i] - primes[i - 1]
                    ans = [primes[i - 1], primes[i]]
        return ans


def main():
    examples = (
        (
            1, 10_000, [2, 3]
        ),
        (
            19, 31, [29, 31]
        ),
        (
            10, 19, [11, 13]
        ),
        (
            4, 6, [-1, -1]
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        left, right, expected = example
        got = solution.closestPrimes(
            left=left,
            right=right,
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
