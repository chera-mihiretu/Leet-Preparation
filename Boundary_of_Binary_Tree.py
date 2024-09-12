from typing import *

class TreeNode:
    def __init__(self, val= 0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left
    def __str__(self):
        current = self
        def getString(root):
            if not root:
                return 'None'
            return f'val: {root.val} [Left: {getString(root.left)}] [Right: {getString(root.right)}]'
        return getString(current)
    
#! This is the solution
class Solution:
    def boundaryOfBinaryTree(self, root:TreeNode) -> List:
        left_bound = []
        right_bound = []
        leaf = []
        def getMeBoundaries(root, type):
            pass
            

            



test_case:List[TreeNode] = []

test_case.append([TreeNode(1, right=TreeNode(2, left=TreeNode(3), right=TreeNode(4))), [1,3,4,2]])
test_case.append([TreeNode(1, left=TreeNode(2, left=TreeNode(3, right=TreeNode(4, left=TreeNode(5), right=TreeNode(6)))), right=TreeNode(7, right=TreeNode(8, left=TreeNode(9, left=TreeNode(10), right=TreeNode(11))))), [1,2,3,4,5,6,10,11,9,8,7,1]])
test_case.append([TreeNode(10, left=TreeNode(5, left=TreeNode(3), right=TreeNode(8, left=TreeNode(7))), right=TreeNode(20, left=TreeNode(18), right=TreeNode(25)))])




if __name__ == '__main__':
    x = Solution()
    
    for index, [test, answer] in enumerate(test_case):
        assert x.boundaryOfBinaryTree(test) == answer
        print('Test case', index + 1, 'Passed')
