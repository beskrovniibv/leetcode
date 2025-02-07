#! /usr/bin/env python

from typing import List


class Solution:
    def tupleSameProduct(self,  nums: List[int]) -> int:
        n = len(nums)
        d = {}
        for i in range(n - 1):
            for j in range(i + 1, n):
                product = nums[i]*nums[j] 
                d[product] = d.get(product, 0) + 1
        result = 0
        for _, v in d.items():
            if v > 1:
                c = v*(v - 1)//2
                result += c*8
        return result


def main():
    examples = (
        (
            [2, 3, 4, 6, 8, 12], 40
        ),
        (
            [2, 3, 4, 6], 8
        ),
        (
            [1, 2, 4, 5, 10], 16
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, expected = example
        got = solution.tupleSameProduct(
            nums=nums,
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
