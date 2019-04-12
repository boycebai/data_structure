#usr/bin/env python
#__coding:utf-8__

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # iteratively
    def mergeTwoLists1(self, l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next


    # recursively
    def mergeTwoLists2(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


    # in-place, iteratively
    def mergeTwoLists(self, l1, l2):
        if None in (l1, l2):
            return l1 or l2
        dummy = cur = ListNode(0)
        dummy.next = l1
        while l1 and l2:
            if l1.val < l2.val:
                l1 = l1.next
            else:
                nxt = cur.next
                cur.next = l2
                tmp = l2.next
                l2.next = nxt
                l2 = tmp
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

if __name__ == "__main__":
    nums = [3,2,2,3]
    val = 2
    A1 = ListNode(1)
    A2 = ListNode(2)
    A3 = ListNode(3)
    A4 = ListNode(4)
    A5 = ListNode(5)
    A1.next = A2
    A2.next = A3
    A3.next = A4
    A4.next = A5

    B1 = ListNode(1)
    B2 = ListNode(2)
    B3 = ListNode(3)
    B4 = ListNode(4)
    B5 = ListNode(5)
    B1.next = B2
    B2.next = B3
    B3.next = B4
    B4.next = B5
    
    solution = Solution()
    result = solution.mergeTwoLists(A1, B2)
    print(result)