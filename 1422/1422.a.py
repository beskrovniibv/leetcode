#! usr/bin/python

# 1422. Maximum Score After Splitting a String

class Solution:
    def maxScore(self, s: str) -> int:
        ones = 0
        zeros = 0
        result = 0
        for c in s:
            ones += int(c == '1')
        for i in range(0, len(s) - 1):
            if s[i] == '1':
                ones -= 1
            else:
                zeros += 1
            result = max(result, ones + zeros)
        return result


if __name__ == '__main__':
    # case 1
    # s = '011101'
    # case 2
    # s = '00111'
    # case 3
    # s = '1111'
    # case 96
    s = '00'

    solution = Solution()
    answer = solution.maxScore(s)
    print(answer)
