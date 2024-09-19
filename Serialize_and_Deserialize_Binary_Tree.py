from typing import *

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        kidType = {'L' : 'L[', 'R': 'R['}
        def serializeThis(root, which):
            if not root.left and not root.right:
                return f'{kidType[which]}{root.val},]'
            answer_left = answer_right = ''
            if root.left:
                answer_left =  serializeThis(root.left, 'L')
            if root.right:
                answer_right= serializeThis(root.right, 'R')
            return f'{kidType[which]}{root.val},{answer_left}{answer_right}]'
        if not root:
            return ''
        return serializeThis(root, 'R')

        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        #print(data)
        dummy = TreeNode(0)
        stack = [dummy]

        pointer = start = 0
        while pointer < len(data):
            #print(stack, pointer, start)
            if data[pointer] != ']':
                start = pointer + 2
                while data[pointer] != ',':
                    pointer += 1
                node = TreeNode(int(data[start:pointer]))
                if data[start - 2] == 'R':
                    stack[-1].right = node
                elif data[start - 2] == 'L':
                    stack[-1].left = node
                stack.append(node)
                pointer += 1
            else:
                stack.pop()
                pointer += 1


        return dummy.right
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))