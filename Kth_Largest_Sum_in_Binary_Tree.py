from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        answer = []
        def getAllLevelSum(root, k):
            if not root: return
            if k == len(answer):
                answer.append(0)
            answer[k] += root.val

            getAllLevelSum(root.left, k + 1)
            getAllLevelSum(root.right, k + 1)
        getAllLevelSum(root, 0)
        answer.sort(reverse=True)
        
        if k-1 >= len(answer):
            return -1
        return answer[k-1]


            