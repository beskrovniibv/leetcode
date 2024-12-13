#! /usr/bin/python python

from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        result = 0
        seq = []
        n = len(nums)
        for idx, el in enumerate(nums):
            seq.append((el, idx))
        seq.sort()
        idx = 0
        while n > 0:
            while nums[seq[idx][1]] < 0:
                idx += 1
            result += seq[idx][0]
            nums[seq[idx][1]] = -1
            n -= 1
            if seq[idx][1] > 0:
                if nums[seq[idx][1] - 1] != -1:
                    n -= 1
                nums[seq[idx][1] - 1] = -1
            if seq[idx][1] < len(nums) - 1:
                if nums[seq[idx][1] + 1] != -1:
                    n -= 1
                nums[seq[idx][1] + 1] = -1
        return result


def main():
    examples = (
        (
            [2, 1, 3, 4, 5, 2], 7
        ),
        (
            [2, 3, 5, 1, 3, 2], 5
        ),
        (
            [10, 44, 10, 8, 48, 30, 17, 38, 41, 27, 16, 33, 45, 45, 34, 30, 22, 3, 42, 42], 212
        )
    )
    solutiuon = Solution()
    for idx, example in enumerate(examples):
        nums, expected = example
        got = solutiuon.findScore(
            nums=nums,
        )
        assert got == expected, f"Error in {idx + 1} sample: expected {expected}, got {got}."

if __name__ == "__main__":
    main()
