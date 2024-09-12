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
        self.res = []
        if not root:
            return self.res
        # root
        if not self.is_leaf(root):
            self.res.append(root.val)

        # left boundary
        t = root.left
        while t:
            if not self.is_leaf(t):
                self.res.append(t.val)
            t = t.left if t.left else t.right

        # leaves
        self.add_leaves(root)

        # right boundary (reverse order)
        s = []
        t = root.right
        while t:
            if not self.is_leaf(t):
                s.append(t.val)
            t = t.right if t.right else t.left
        while s:
            self.res.append(s.pop())

        # output
        return self.res

    def add_leaves(self, root):
        if self.is_leaf(root):
            self.res.append(root.val)
            return
        if root.left:
            self.add_leaves(root.left)
        if root.right:
            self.add_leaves(root.right)

    def is_leaf(self, node) -> bool:
        return node and node.left is None and node.right is None
            

            



test_case:List[TreeNode] = []

test_case.append([TreeNode(1, right=TreeNode(2, left=TreeNode(3), right=TreeNode(4))), [1,3,4,2]])
test_case.append([TreeNode(1, left=TreeNode(2, left=TreeNode(3, right=TreeNode(4, left=TreeNode(5), right=TreeNode(6)))), right=TreeNode(7, right=TreeNode(8, left=TreeNode(9, left=TreeNode(10), right=TreeNode(11))))), [1,2,3,4,5,6,10,11,9,8,7]])
test_case.append([TreeNode(10, left=TreeNode(5, left=TreeNode(3), right=TreeNode(8, left=TreeNode(7))), right=TreeNode(20, left=TreeNode(18), right=TreeNode(25))), [10, 5, 3, 7, 18, 25, 20]])
test_case.append([TreeNode(1, right=TreeNode(2, right=TreeNode(3, right=TreeNode(8, right=TreeNode(9)), left=TreeNode(4, left=TreeNode(5, left=TreeNode(6), right=TreeNode(7)))))), [1, 6,7,9,8,3,2]])
test_case.append([TreeNode(1, right=TreeNode(2, right=TreeNode(3, right=TreeNode(4, TreeNode(5, right=TreeNode(6)))))), [1,6,5,4,3,2]])
test_case.append([TreeNode(1), [1]])

if __name__ == '__main__':
    x = Solution()
    
    for index, [test, answer] in enumerate(test_case):
        cur_ans = x.boundaryOfBinaryTree(test)
        assert cur_ans == answer, f'expected: {answer} got: {cur_ans}'
        print('Test case', index + 1, 'Passed')
