from typing import *

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        nodeColor = [-1] * len(graph)
        def dfs(curr_node, paint):
            if nodeColor[curr_node] == -1:
                nodeColor[curr_node] = paint
            else:
                if nodeColor[curr_node] != paint:
                    return False
                else:
                    return True
            for node in graph[curr_node]:
                if not dfs(node, int(not paint)):
                    return False
            return True
        for i in range(len(nodeColor)):
            if nodeColor[i] == -1:
                if not dfs(i,0):
                    return False
        return True
            