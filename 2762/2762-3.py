#! /usr/bin/python python

from typing import List


class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:
        ans = 1
        left = nums[0] - 2
        right = nums[0] + 2
        l = 0
        for r in range(1, len(nums)):
            if left <= nums[r] <= right:
                left = max(left, nums[r] - 2)
                right = min(right, nums[r] + 2)
            else:
                left = nums[r] - 2
                right = nums[r] + 2
                l = r
                while nums[r] - 2 <= nums[l] <= nums[r] + 2:
                    left = max(left, nums[l] - 2)
                    right = min(right, nums[l] + 2)
                    l -= 1
                l += 1
            print(nums[l:r], ans, r - l + 1)
            ans += r - l + 1
        return ans


def main():
    examples = (
        # (
        #     [5, 4, 2, 4], 8
        # ),
        # (
        #     [1, 2, 3], 6
        # ),
        (
            [3, 1, 3, 5, 1, 3], 11
        ),
        # (
        #     [12, 13, 14, 13, 12, 11, 10, 10, 12, 11, 10, 11, 9, 14], 56
        # ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, expected = example
        got = solution.continuousSubarrays(
            nums=nums
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
