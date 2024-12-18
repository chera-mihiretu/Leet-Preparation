from typing import *

class SegmentTree:
    def __init__(self, number):
        self.size = number
        self.tree = [0] * (self.size * 4)
        
    def change(self, number):
        self.update(0, 0, self.size, number)
    def update(self, node, left, right, index):
        if left == right:
            self.tree[node] += 1
            return 
        mid = (right + left) // 2
        
        left_child, right_child = self.getChild(node)
        if index <= mid:
            self.update(left_child, left, mid, index)
        else:
            self.update(right_child, mid + 1, right, index)
        self.tree[node] = self.tree[left_child] + self.tree[right_child]
    def getMax(self, node, q_left, q_right, left, right):
        if q_left > q_right:
            return 0
        mid = (left + right) // 2
        left_child, right_child = self.getChild(node)
        
        if q_left == left and q_right == right:
            return self.tree[node]
        l = self.getMax(left_child, q_left, min(mid, q_right), left, mid)
        r = self.getMax(right_child, max(q_left, mid + 1), q_right, mid + 1, right)
        return l + r
    def getChild(self, node):
        return node * 2 + 1, node * 2 + 2 

    def query(self, start):

        return self.getMax(0, 0, start - 1, 0, self.size)




    
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # setting offset
        minimum = min(nums)
        if minimum < 0:
            for i in range(len(nums)):
                nums[i] += abs(minimum) + 1
        
        # get answer
        answer = [0] * len(nums)
        seg = SegmentTree(max(nums))

        for i in range(len(nums)-1, -1, -1):
            
            seg.change(nums[i])
            answer[i] = seg.query(nums[i])
            
            
        return answer

        