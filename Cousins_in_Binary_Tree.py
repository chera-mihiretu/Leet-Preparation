from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sums = []
        def getAllSums(root, array, level):
            if not root:
                return 
            if level == len(array):
                array.append(0)
            
            array[level] += root.val

            getAllSums(root.left, array, level + 1)
            getAllSums(root.right, array, level + 1)
        

        def modifyCousins(root, new_tree, prev, is_left, level):
            nonlocal sums
            current_val = sums[level]
            if prev:
                if is_left:
                    if prev.right:
                        current_val -= prev.right.val
                else:
                    if prev.left:
                        current_val -= prev.left.val
            current_val -= root.val
            new_tree.val = current_val
            if root.left:
                new_tree.left = TreeNode(0)
                modifyCousins(root.left, new_tree.left,root, True, level + 1)
            if root.right:
                new_tree.right = TreeNode(0)
                modifyCousins(root.right, new_tree.right,root, False, level + 1)

        getAllSums(root, sums, 0)

        new_tree = TreeNode(0)

        modifyCousins(root, new_tree, None, sums, 0)

        return new_tree