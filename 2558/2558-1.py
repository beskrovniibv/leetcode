#! /usr/bin/python python
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        result = sum(gifts)
        for _ in range(k):
            gifts.sort()
            pile = gifts[-1]
            leave = int(pile**0.5)
            result -= pile - leave
            gifts[-1] = leave
        return result


def main():
    examples = (
        (
            [25, 64, 9, 4, 100], 4, 29
        ),
        (
            [1, 1, 1, 1], 4, 4
        )
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        gifts, k, expected = example
        got = solution.pickGifts(
            gifts=gifts,
            k=k
        )
        assert got == expected, f"Error in sample: {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
