#! usr/bin/python

# 1436. Destination City

from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        _from = set()
        _to = set()
        for pair in paths:
            _from.add(pair[0])
            _to.add(pair[1])
        return list(_to - _from)[0]


if __name__ == '__main__':
    # case 1
    # paths = [['London', 'New York'], ['New York', 'Lima'], ['Lima', 'Sao Paulo']]
    # case 2
    # paths = [['B', 'C'], ['D', 'B'], ['C', 'A']]
    # case3
    paths = [['A', 'Z']]

    solution = Solution()
    answer = solution.destCity(paths)
    print(answer)
