#! /usr/bin/env python

from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        result = []
        n, m = len(nums1), len(nums2)
        i, j = 0, 0
        while i < n or j < m:
            if i < n and j < m:
                n1, n2 = nums1[i], nums2[j]
                if n1[0] == n2[0]:
                    result.append([n1[0], n1[1] + n2[1]])
                    i += 1
                    j += 1
                elif n1[0] < n2[0]:
                    result.append([n1[0], n1[1]])
                    i += 1
                else:
                    result.append([n2[0], n2[1]])
                    j += 1
            elif i < n:
                n1 = nums1[i]
                result.append([n1[0], n1[1]])
                i += 1
            elif j < m:
                n2 = nums2[j]
                result.append([n2[0], n2[1]])
                j += 1
        return result


def main():
    examples = (
        (
            [[1, 2], [2, 3], [4, 5]], [[1, 4], [3, 2], [4, 1]], [[1, 6], [2, 3], [3, 2], [4, 6]]
        ),
        (
            [[2, 4], [3, 6], [5, 5]], [[1, 3], [4, 3]], [[1, 3], [2, 4], [3, 6], [4, 3], [5, 5]]
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums1, nums2, expected = example
        got = solution.mergeArrays(
            nums1=nums1,
            nums2=nums2
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
