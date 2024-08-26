from typing import *

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        answer = []
        
        def traverse(root):
            if not root:
                return
            for i in range(len(root.children)):
                traverse(root.children[i])
            answer.append(root.val)
        traverse(root)
        return answer
            