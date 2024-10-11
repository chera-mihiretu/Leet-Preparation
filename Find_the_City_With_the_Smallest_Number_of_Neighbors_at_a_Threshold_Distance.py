from typing import *

from typing import List

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = [[float('inf') for i in range(n)] for i in range(n)]
        for i in range(n):
            graph[i][i] = 0
        for fr, to, we in edges:
            graph[fr][to] = we
            graph[to][fr] = we
        


        for i in range(n):
            for j in range(n):
                for k in range(n):
                    graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
        answer = (float('inf'), 0) # distance , node
        for i in range(n):
            count = 0
            for j in range(n):
                if graph[i][j] <= distanceThreshold:
                    count += 1
            if count <= answer[0]:
                answer = [count, i]
        return answer[-1]