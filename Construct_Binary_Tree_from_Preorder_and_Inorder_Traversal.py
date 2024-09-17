from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        que = deque(preorder)
        def devide(left, right):
            if left > right:
                return None
            if left == right:
                que.popleft()
                return TreeNode(inorder[left])
            head = que.popleft()
            #print(head, inorder[left: right + 1])
            search_index = inorder[left: right + 1].index(head)
            toleft = devide(left, left + search_index - 1)
            toright = devide(left + search_index + 1, right)
            root = TreeNode(head, toleft, toright)
            return root
        return devide(0, len(inorder) - 1)


            

            
            
             
