class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0
        for n1 in nums1:
            for n2 in nums2:
                result ^= n1 ^ n2
        return result