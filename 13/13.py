#! usr/bin/python

# 13. Roman to Integer


class Solution:
    def romanToInt(self, s: str) -> int:
        converter = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900,
        }
        i = 0
        result = 0
        while i < len(s):
            c = s[i: i + 2]
            if c in converter:
                result += converter[c]
                i += 2
            else:
                result += converter[c[0]]
                i += 1
        return result


if __name__ == '__main__':
    s = input()
    solution = Solution()
    print(solution.romanToInt(s))
