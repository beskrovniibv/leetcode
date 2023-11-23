#! usr/bin/python

# 83. Remove Duplicates from Sorted List

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        el = self
        while el is not None:
            print(el.val, end=' ')
            el = el.next
        print()


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        el = head
        while el.next is not None:
            if el.next.val == el.val:
                el.next = el.next.next
            else:
                el = el.next
        return head


if __name__ == '__main__':
    head = None
    for value in map(int, input().split()):
        if not head:
            el = ListNode(value)
            head = el
        else:
            el = head
            while el.next is not None:
                el = el.next
            el.next = ListNode(value)
    solution = Solution()
    head.print()
    unique = solution.deleteDuplicates(head)
    unique.print()
