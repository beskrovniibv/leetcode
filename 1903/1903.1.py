#! usr/bin/python

# 1903. Largest Odd Number in String

ODD = '13579'


class Solution:
    def largestOddNumber(self, num: str) -> str:
        i = len(num) - 1
        while num[i] not in ODD and i >= 0:
            i -= 1
        return num[:(i + 1)]


if __name__ == '__main__':
    # case 1
    # num = '52'
    # case 2
    # num = '4206'
    # case 3
    num = '35427'

    solution = Solution()
    answer = solution.largestOddNumber(num)
    print(answer)
