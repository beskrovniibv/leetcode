#! usr/bin/python

# 205. Isomorphic Strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        transform1 = {}
        transform2 = {}
        n = len(s)
        for i in range(n):
            cs = s[i]
            ct = t[i]
            transform1[cs] = transform1.get(cs, ct)
            transform2[ct] = transform2.get(ct, cs)
            if transform1[cs] != ct or transform2[ct] != cs:
                return False
        return True


if __name__ == '__main__':
    # case 1
    # s = 'egg'
    # t = 'add'
    # case 2
    # s = 'foo'
    # t = 'bar'
    # case 3
    # s = 'paper'
    # t = 'title'
    # case 37
    s = 'badc'
    t = 'baba'

    solution = Solution()
    answer = ('false', 'true')[solution.isIsomorphic(s, t)]
    print(answer)
