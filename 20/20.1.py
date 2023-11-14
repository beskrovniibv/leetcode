#! usr/bin/python

# 20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        flag = True
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if c == ')':
                    flag = len(stack) != 0 and stack[-1] == '('
                    if not flag:
                        break
                elif c == ']':
                    flag = len(stack) != 0 and stack[-1] == '['
                    if not flag:
                        break
                elif c == '}':
                    flag = len(stack) != 0 and stack[-1] == '{'
                    if not flag:
                        break
                stack.pop()
        flag = flag and len(stack) == 0
        return flag


if __name__ == '__main__':
    s = input()
    solution = Solution()
    print(solution.isValid(s))
