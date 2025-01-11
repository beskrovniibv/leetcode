#! /usr/bin/python python python3

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        if k > n:
            return False
        counter = set()
        for c in s:
            counter.symmetric_difference_update(c)
        return len(counter) <= k


def main():
    examples = (
        (
            "annabelle", 2, True
        ),
        (
            "leetcode", 3, False
        ),
        (
            "true", 4, True
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        s, k, expected = example
        got = solution.canConstruct(
            s=s,
            k=k
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
