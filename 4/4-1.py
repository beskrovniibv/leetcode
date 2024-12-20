from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        s = 0
        n1 = len(nums1)
        n2 = len(nums2)
        m = ((n1 + n2) // 2,) if (n1 + n2) & 1 == 1 else ((n1 + n2) // 2 - 1, (n1 + n2) // 2)
        n = len(m)
        i, j = 0, 0
        i1 = 0
        i2 = 0
        while j < n:
            if i1 < len(nums1) and i2 < len(nums2):
                if nums1[i1] < nums2[i2]:
                    if i == m[j]:
                        s += nums1[i1]
                        j += 1
                    i1 += 1
                else:
                    if i == m[j]:
                        s += nums2[i2]
                        j += 1
                    i2 += 1
            elif i1 < len(nums1):
                if i == m[j]:
                    s += nums1[i1]
                    j += 1
                i1 += 1
            elif i2 < len(nums2):
                if i == m[j]:
                    s += nums2[i2]
                    j += 1
                i2 += 1
            i += 1
        return s/n


def main():
    examples = (
        (
            [1, 3], [2], 2.00000
        ),
        (
            [1, 2], [3, 4], 2.50000
        ),
        (
            [0, 0], [0, 0], 0.0
        ),
        (
            [2, 2, 4, 4], [2, 2, 2, 4, 4], 2.0
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums1, nums2, expected = example
        got = solution.findMedianSortedArrays(
            nums1=nums1,
            nums2=nums2
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}"

if __name__ == "__main__":
    main()
