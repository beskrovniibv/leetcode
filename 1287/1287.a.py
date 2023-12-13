#! usr/bin/python

# 1287. Element Appearing More Than 25% In Sorted Array

from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        mx, cur = 1, 1
        last = arr[0]
        result = last
        for i in range(1, len(arr)):
            if arr[i] == last:
                cur += 1
            else:
                if cur > mx:
                    mx = cur
                    result = last
                last = arr[i]
                cur = 1
        if cur > mx:
            result = last
        return result
