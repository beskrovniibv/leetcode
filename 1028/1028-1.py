#! /usr/bin/env python

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        l = f"{self.left.val}" if self.left else "None"
        r = f"{self.right.val}" if self.right else "None"
        return f"({self.val}: ({l}), ({r}))"


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        n = len(traversal)
        st = []
        i = 0
        while i < n:
            value = 0
            depth = 0
            while i < n and traversal[i] == "-":
                depth += 1
                i += 1
            while i < n and traversal[i] in '0123456789':
                value = value*10 + int(traversal[i])
                i += 1
            node = TreeNode(value)
            while len(st) > depth:
                st.pop()
            if st:
                parent = st[-1]
                if not parent.left:
                    parent.left = node
                else:
                    parent.right = node
            st.append(node)
        return st[0]


def main():
    solution = Solution()
    solution.recoverFromPreorder(
        traversal="1-2--3--4-5--6--7"
    )


if __name__ == "__main__":
    main()
