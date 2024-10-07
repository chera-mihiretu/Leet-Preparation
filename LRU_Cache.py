from typing import *

class Node:
    def __init__(self, key, val):
        self.val, self.key = val, key
        self.next, self.prev = None, None
    def __str__(self):
        curr = self
        def helper(node):
            if not node:
                return 'None'
            return f'[next:[val:{node.val}, key:{node.key}], {helper(node.next)}]'
        return helper(curr)
    
class LRUCache:
    def __init__(self, capacity: int):
        self.head, self.tail = Node(0,0), Node(0,0)
        self.head.next, self.tail.prev = self.tail, self.head
        self.map = {}
        self.cap, self.curr = capacity, 0
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        prev = node.prev
        node.next, node.prev = None, None
        return node
    def addNode(self, node, to):
        hold = to.prev
        to.prev = node
        node.next = to
        hold.next = node
        node.prev = hold
    def removeLast(self):
        hold = self.tail.prev
        self.map.pop(hold.key)
        self.curr -= 1
        self.removeNode(hold)

    def get(self, key: int) -> int:
        # print(self.head)
        if key in self.map:
            node = self.map[key]
            if node.prev != self.head:
                node = self.removeNode(node)
                self.addNode(node, self.head.next)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            if self.curr == self.cap:
                self.removeLast()
            
            self.map[key] = Node(key, value)
            self.addNode(self.map[key], self.head.next)
            self.curr += 1
        else:
            node =  self.map[key]
            node.val = value
            if node.prev != self.head:
                node = self.removeNode(node)
                
                self.addNode(node, self.head.next)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)