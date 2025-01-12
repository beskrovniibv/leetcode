#! /usr/bin/python python python3

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        opened = []
        unlocked = []

        for i, (ch, state) in enumerate(zip(s, locked)):
            if state == "0":
                unlocked.append(i)
            elif ch == "(":
                opened.append(i)
            else:
                if opened:
                    opened.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False
        while opened and unlocked and opened[-1] < unlocked[-1]:
            opened.pop()
            unlocked.pop()
        return not opened and len(unlocked) & 1 == 0


def main():
    examples = (
        (
            "(())", "0101", True
        ),
        (
            "((()(()()))()((()()))))()((()(()", "10111100100101001110100010001001", True
        ),
        (
            ")(", "00", True
        ),
        (
            "))()))", "010100", True
        ),
        (
            "()()", "0000", True
        ),
        (
            ")", "0", False
        ),
        (
            "()))", "0010", True
        ),
        (
            ")", "0", False
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        s, locked, expected = example
        got = solution.canBeValid(
            s=s,
            locked=locked
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
