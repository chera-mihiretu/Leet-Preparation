from typing import *

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for i in range(numCourses)]
        prer = [set() for i in range(numCourses)]
        visited = [False for i in range(numCourses)]
        def dfs(node):
            cur = set()
            if visited[node]:
                return prer[node] | {node}

            for child in graph[node]:
                cur |= dfs(child)
            visited[node] = True
            prer[node] = cur.copy()
            cur.add(node)
            return cur
        for fr, to in prerequisites:
            graph[fr].append(to)
        
        for i in range(numCourses):
            if not visited[i]:
                dfs(i)
        answer = [False for i in range(len(queries))]
        for i, (fr, to )in enumerate(queries):
            if to in prer[fr]:
                answer[i] = True


        print(prer)
        return answer
        