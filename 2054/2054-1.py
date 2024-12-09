#! /usr/bin/python python

from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        answer = 0
        mx = 0
        facts = []
        for event in events:
            start, end, value = event
            facts.append((start, 1, value))
            facts.append((end + 1, 0, value))
        facts.sort()

        for fact in facts:
            _, started, value = fact
            if started:
                answer = max(answer, value + mx)
            else:
                mx = max(mx, value)
        return answer


def main():
    solution = Solution()
    examples = (
        (
            [[1, 3, 2], [4, 5, 2], [2, 4, 3]], 4
        ),
        (
            [[1, 3, 2], [4, 5, 2], [1, 5, 5]], 5
        ),
        (
            [[1, 5, 3], [1, 5, 1], [6, 6, 5]], 8
        ),
    )
    for index, example in enumerate(examples):
        events, expected = example
        get = solution.maxTwoEvents(
            events=events
        )
        assert get == expected, f"Error in sample: {index + 1}: expected {expected}, got {get}."


if __name__ == "__main__":
    main()
