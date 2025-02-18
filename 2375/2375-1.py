#! /usr/bin/env python

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        result = []
        st = []
        for i in range(1, n + 2):
            st.append(i)
            if i == n + 1 or pattern[i - 1] == "I":
                while st:
                    result.append(st.pop())
        return "".join(map(str, result))


def main():
    examples = (
        (
            "IIIDIDDD", "123549876"
        ),
        (
            "DDD", "4321"
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        pattern, expected = example
        got = solution.smallestNumber(
            pattern=pattern
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
