#! /usr/bin/python python python3

from collections import deque
from typing import List


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        sorted_nums = sorted(nums)
        group_id = 0
        groups = {}
        lists = [deque([])]
        prev = None
        for num in sorted_nums:
            if not prev:
                prev = num
                groups[prev] = group_id
                lists[group_id].append(prev)
                continue
            if abs(num - prev) > limit:
                group_id += 1
                lists.append(deque([]))
            prev = num
            groups[prev] = group_id
            lists[group_id].append(prev)
        result = []
        for num in nums:
            result.append(lists[groups[num]].popleft())
        return result


def main():
    examples = (
        (
            [1, 60, 34, 84, 62, 56, 39, 76, 49, 38], 4, [1, 56, 34, 84, 60, 62, 38, 76, 49, 39]
        ),
        (
            [1, 5, 3, 9, 8], 2, [1, 3, 5, 8, 9]
        ),
        (
            [1, 7, 6, 18, 2, 1], 3, [1, 6, 7, 18, 1, 2]
        ),
        (
            [1, 7, 28, 19, 10], 3, [1, 7, 28, 19, 10]
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, limit, expected = example
        got = solution.lexicographicallySmallestArray(
            nums=nums,
            limit=limit
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
