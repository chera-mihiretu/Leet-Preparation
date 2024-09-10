from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ppp = None
        current = head
        while current:
            hold = current.next
            current.next = ppp
            if ppp:
                current.next = ListNode(gcd(current.val, ppp.val), ppp)
            ppp = current
            current = hold
        ppp, current = None, ppp
        while current:
            hold = current.next
            current.next = ppp
            ppp = current
            current = hold
        return ppp