from typing import *
from heapq import * 

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        """
            0.2 0.5 
        """
        # graph
        graph = [[] for i in range(n)]
        # distance 
        distances = [float('-inf') for i in range(n)]
        # processed 
        processed = [False for i in range(n)]
        # heap 
        for i,[ fr, to] in enumerate(edges):
            graph[to].append([fr, succProb[i]])
            graph[fr].append([to, succProb[i]])
        
        max_heap = [(-1, start)]

        while max_heap:
            current_mul, current_node = heappop(max_heap)

            if processed[current_node]:
                continue
            processed[current_node] = True

            for child, weight in graph[current_node]:
                mul = - weight * current_mul
                if mul > distances[child]:
                    distances[child] = mul
                    heappush(max_heap, [-mul, child])
        answer = distances[end]
        return answer if answer != float('-inf') else 0



                    

