from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # add to set to grab it quickly 
        nums_in_set = set(nums)
        dummy = ListNode(None, next=head)
        current = dummy
        while current.next:
            if current.next.val in nums_in_set:
                current.next = current.next.next
            else:
                current = current.next
        return dummy.next