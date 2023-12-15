#! usr/bin/python

# 160. Intersection of Two Linked Lists

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        n, m = 0, 0
        node = headA
        while node:
            n += 1
            node = node.next
        node = headB
        while node:
            m += 1
            node = node.next
        if m > n:
            long = headB
            short = headA
            l, s = m, n
        else:
            long = headA
            short = headB
            l, s = n, m
        for i in range(l - s):
            long = long.next
        while long and short:
            if long == short:
                return long
            long = long.next
            short = short.next
        return None


if __name__ == '__main__':
    # case 1
    a = ListNode(4)
    a.next = ListNode(1)
    c = a.next.next = ListNode(8)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = ListNode(5)
    b = ListNode(5)
    b.next = ListNode(6)
    b.next.next = ListNode(1)
    b.next.next.next = c

    solution = Solution()
    answer = solution.getIntersectionNode(a, b)
    print(answer.val if answer else 'None')
