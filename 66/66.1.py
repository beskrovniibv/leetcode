#! usr/bin/path

# 66. Plus One

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        partial = digits[-1] + 1
        result = [partial % 10]
        partial //= 10
        for i in range(len(digits) - 2, -1, -1):
            digit = digits[i]
            partial = digit + partial
            result.append(partial % 10)
            partial //= 10
        if partial:
            result.append(partial)
        return reversed(result)


if __name__ == '__main__':
    digits = list(map(int, input().split()))
    solution = Solution()
    answer = solution.plusOne(digits)
    print(*answer)
