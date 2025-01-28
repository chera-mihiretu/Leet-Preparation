from typing import *

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        def dfs(row, col):
            if not inbound(row, col) or grid[row][col] == 0:
                return 0
            hold = grid[row][col] 
            grid[row][col] = 0
            
            for x, y in dirs:
                hold += dfs(row + x, col + y)
            return hold
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                answer = max(answer, dfs(i, j))
        return answer
        