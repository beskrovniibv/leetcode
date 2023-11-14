#! usr/bin/python

# 21. Merge Two Sorted Lists

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        l = None
        l1, l2 = list1, list2
        while l1 is not None:
            if l1.val <= l2.val:
                val = l1.val
                l1 = l1.next
            else:
                val = l2.val
                l2 = l2.next
            # new = ListNode(val)
            if l is None:
                l = ListNode(val, None)
                last = l
            else:
                last.next = ListNode(val, None)
                last = last.next
            if l2 is None or l1 is None:
                break
        while l1 is not None:
            last.next = ListNode(l1.val, None)
            l1 = l1.next
            last = last.next
        while l2 is not None:
            last.next = ListNode(l2.val, None)
            l2 = l2.next
            last = last.next
        return l


if __name__ == '__main__':
    l1, l2 = None, None
    for v in map(int, input().split()):
        if l1 is None:
            l1 = ListNode(v, None)
            last = l1
        else:
            last.next = ListNode(v, None)
            last = last.next
    for v in map(int, input().split()):
        if l2 is None:
            l2 = ListNode(v, None)
            last = l2
        else:
            last.next = ListNode(v, None)
            last = last.next
    solution = Solution()
    l = solution.mergeTwoLists(l1, l2)
    while l is not None:
        print(l.val, sep='', end=' ')
        l = l.next
