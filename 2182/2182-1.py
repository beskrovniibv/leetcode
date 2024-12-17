#! /usr/bin/python python

from heapq import heapify, heappop, heappush


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        letters = {}
        heap = []
        result = []
        for ch in s:
            letters[ch] = letters.get(ch, 0) + 1
        for letter, count in letters.items():
            heap.append([-ord(letter), count])
        heapify(heap)
        seq = 0
        st = []
        while True:
            if not heap or not st and len(heap) == 1 and seq == repeatLimit:
                break
            ch, count = heappop(heap)
            if st:
                while st:
                    heappush(heap, st.pop())
                stack = True
            else:
                stack = False
            if seq < repeatLimit:
                result.append(chr(-ch))
                seq += 1
                if count - 1:
                    heappush(heap, [ch, count - 1])
                else:
                    seq = 0
            else:
                st.append([ch, count])
                seq = 0
            if stack:
                seq = 0
                stack = False
        return "".join(result)


def main():
    examples = (
        (
            "cczazcc", 3, "zzcccac"
        ),
        (
            "aababab", 2, "bbabaa"
        ),
        (
            "robnsdvpuxbapuqgopqvxdrchivlifeepy", 2, "yxxvvuvusrrqqppopponliihgfeeddcbba"
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        s, repeatLimit, expected = example
        got = solution.repeatLimitedString(
            s=s,
            repeatLimit=repeatLimit
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
