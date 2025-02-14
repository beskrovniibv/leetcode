#! /usr/bin/env python

from collections import deque
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        result = 0
        q1 = deque(sorted(nums))
        q2 = deque([])
        data = [q1.popleft(), q1.popleft()]
        j1, j2 = data
        b = False
        while j1 < k or j2 < k:
            result += 1
            v = min(j1, j2)*2 + max(j1, j2)
            q2.append(v)
            for i in range(2):
                if q1 and q2:
                    if q1[0] < q2[0]:
                        data[i] = q1.popleft()
                    else:
                        data[i] = q2.popleft()
                elif q1:
                    data[i] = q1.popleft()
                elif q2:
                    data[i] = q2.popleft()
                else:
                    b = True
                    break
            if b:
                break
            j1, j2 = data
        return result


def main():
    examples = (
        (
            [2, 11, 10, 1, 3], 10, 2
        ),
        (
            [1, 1, 2, 4, 9], 20, 4
        ),
        (
            [999999999, 999999999, 999999999], 1000000000, 2
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        nums, k, expected = example
        got = solution.minOperations(
            nums=nums,
            k=k
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
