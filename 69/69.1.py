#! usr/bin/python

# 69. Sqrt(x)

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x + 1
        while right - left > 1:
            middle = (left + right) // 2
            if middle**2 > x:
                right = middle
            else:
                left = middle
        return left


if __name__ == '__main__':
    x = int(input())
    solution = Solution()
    answer = solution.mySqrt(x)
    print(answer)
