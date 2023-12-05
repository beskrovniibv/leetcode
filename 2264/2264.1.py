#! usr/bin/python

# 2264. Largest 3-Same-Digit Number in String

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = ''
        fmin = None
        for i in range(len(num) - 2):
            subnum = num[i:i + 3]
            if len(set(subnum)) == 1:
                if not fmin:
                    fmin = int(subnum)
                    result = subnum
                else:
                    min = int(subnum)
                    if min > fmin:
                        fmin = min
                        result = subnum
        return result


if __name__ == '__main__':
    # case 1
    num = '6777133339'

    solution = Solution()
    answer = solution.largestGoodInteger(num)
    print(answer)
