#! /usr/bin/python python python3

from typing import List


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        result = [None, None, None]
        n = len(nums)
        psum = [0] + [0]*n
        for i in range(n):
            psum[i + 1] = psum[i] + nums[i]
        mx = 0
        for i in range(n - 2*k):
            _sum1 = psum[i + k] - psum[i]
            for j in range(i + k, n - 2*k + 1):
                _sum2 = psum[j + k] - psum[j]
                for l in range(j + k, n - k + 1):
                    _sum3 = psum[l + k] - psum[l]
                    if _sum1 + _sum2 + _sum3 > mx:
                        mx = _sum1 + _sum2 + _sum3
                        result[0] = i
                        result[1] = j
                        result[2] = l
        return result


def main():
    examples = (
        (
            [1, 2, 1, 2, 6, 7, 5, 1], 2, [0, 3, 5]
        ),
        (
            [1, 2, 1, 2, 1, 2, 1, 2, 1], 2, [0, 2, 4]
        ),
        (
            [7, 13, 20, 19, 19, 2, 10, 1, 1, 19], 3, [1, 4, 7]
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, k, expected = example
        got = solution.maxSumOfThreeSubarrays(
            nums=nums,
            k=k
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
