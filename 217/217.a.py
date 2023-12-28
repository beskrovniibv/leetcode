#! usr/bin/python

# 217. Contains Duplicate

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = dict()
        for num in nums:
            if n.get(num, 0) != 0:
                return True
            n[num] = n.get(num, 0) + 1
        return False


if __name__ == '__main__':
    pass
