#! usr/bin/path

# 1496. Path Crossing

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = {(0, 0)}
        x, y = 0, 0
        for move in path:
            if move == 'N':
                y += 1
            elif move == 'E':
                x += 1
            elif move == 'S':
                y -= 1
            elif move == 'W':
                x -= 1
            else:
                assert False, 'invalid direction'
            if (x, y) in visited:
                return True
            visited.add((x, y))
        return False


if __name__ == '__main__':
    # case 1
    path = 'NES'
    # case 2
    # path = 'NESWW'

    solution = Solution()
    answer = solution.isPathCrossing(path)
    print(('false', 'true')[answer])
