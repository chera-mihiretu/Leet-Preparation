from typing import *
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges)))
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            _x, _y = find(x), find(y)

            if _x == _y:
                return [x + 1, y + 1]
            parent[_x] = _y
        for fr, to in edges:
            result = union(fr - 1, to - 1)
            if  result != None:
                return result
        return []