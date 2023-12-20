#! usr/bin/python

# 171. Excel Sheet Column Number

from string import ascii_uppercase as abc


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        m = 1
        size = len(abc)
        for c in reversed(columnTitle):
            p = (abc.index(c) + 1) * m
            result += p
            m *= size
        return result


if __name__ == '__main__':
    # case 1
    # columnTitle = 'A'
    # case 1
    # columnTitle = 'AB'
    # case 3
    columnTitle = 'ZY'

    solution = Solution()
    answer = solution.titleToNumber(columnTitle)
    print(answer)
