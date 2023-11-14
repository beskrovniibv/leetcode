from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], index]
            seen[num] = index


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    target = int(input())
    solution = Solution()
    print(solution.twoSum(nums, target))
