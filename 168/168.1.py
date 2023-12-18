#! usr/bin/python

# 168. Excel Sheet Column Title

from string import ascii_uppercase as abc


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        size = len(abc)
        while columnNumber > 0:
            result.append(abc[(columnNumber - 1) % size])
            columnNumber = (columnNumber - 1) // size
        return ''.join(reversed(result))


if __name__ == '__main__':
    # case 1
    # columnNumber = 1
    # case 2
    columnNumber = 28
    # case 3
    # columnNumber = 701

    solution = Solution()
    answer = solution.convertToTitle(columnNumber)
    print(answer)
