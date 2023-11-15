#! usr/bin/python

# 28. Find the Index of the First Occurrence in a String

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        result = -1
        i = 0
        while i < len(haystack):
            start = i
            while haystack[i] == needle[i - start]:
                i += 1
                if (i - start) == len(needle):
                    return start
                if i == len(haystack):
                    return -1
            else:
                i = start
            i += 1
        return result


if __name__ == '__main__':
    haystack = input()
    needle = input()
    solution = Solution()
    print(solution.strStr(haystack=haystack, needle=needle))
