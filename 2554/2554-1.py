#! /usr/bin/python

from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        result = 0
        summ = 0
        for i in range(1, n + 1):
            if i not in banned and summ + i <= maxSum:
                summ += i
                result += 1
        return result


def main():
    solution = Solution()
    examples = (
        (
            1, [1, 6, 5], 5, 6, 2
        ),
        (
            2, [1, 2, 3, 4, 5, 6, 7], 8, 1, 0
        ),
        (
            3, [11], 7, 50, 7
        )
    )
    for example in examples:
        index, banned, n, maxSum, answer = example
        assert solution.maxCount(
            banned=banned,
            n=n,
            maxSum=maxSum
        ) == answer, f"Ошибка в примере {index}"


if __name__ == "__main__":
    main()
