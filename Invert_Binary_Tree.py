from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        my_root = TreeNode(root.val)
        def invert(new_root, root):
            if root.right:
                new_root.left = TreeNode(root.right.val)
                invert(new_root.left, root.right)
            if root.left:
                new_root.right = TreeNode(root.left.val)
                invert(new_root.right, root.left)

        invert(my_root, root)
        return my_root