#! usr/bin/python

# 1716. Calculate Money in Leetcode Bank

class Solution:
    def totalMoney(self, n: int) -> int:
        result = 0
        monday = 1
        for i in range(1, n + 1):
            if (i - 1) % 7 == 0:
                result += monday
                current = monday
                monday += 1
            else:
                current += 1
                result += current
        return result


if __name__ == '__main__':
    # case 1
    # n = 4
    # case 2
    # n = 10
    # case 2
    n = 20

    solution = Solution()
    answer = solution.totalMoney(n)
    print(answer)
