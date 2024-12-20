from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pass


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
