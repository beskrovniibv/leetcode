#! usr/bin/python

# 171. Excel Sheet Column Number

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        abc = {
            'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,
            'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
            'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22,
            'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
        result = 0
        m = 1
        size = len(abc)
        for i in range(len(columnTitle) - 1, -1, -1):
            c = columnTitle[i]
            p = abc[c] * m
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
