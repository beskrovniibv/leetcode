#! /usr/bin/env python

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        st = [""]
        idx = 0
        while st:
            s = st.pop()
            if len(s) == n:
                idx += 1
                if idx == k:
                    return s
                continue
            for ch in "cba":
                if len(s) == 0 or s[-1] != ch:
                    st.append(s + ch)
        return ""


def main():
    examples = (
        (
            1, 3, "c"
        ),
        (
            1, 4, ""
        ),
        (
            3, 9, "cab"
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        n, k, expected = example
        got = solution.getHappyString(
            n=n,
            k=k
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
