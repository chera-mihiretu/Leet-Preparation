from typing import *
from collections import deque 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maximum = float('-inf')
        max_level = 0
        level = 0
        que = deque([root])
        while que:
            x = len(que)
            current = 0
            level += 1
            for i in range(x):
                node = que.popleft()
                current += node.val
                if node.right:
                    que.append(node.right)
                if node.left:
                    que.append(node.left)
            if current > maximum:
                maximum = current 
                max_level = level
        return max_level


