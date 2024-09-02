from typing import *
from collections import deque

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        que = deque()
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        def inbound(row, col):
            return 0 <= row < len(isWater) and 0 <= col < len(isWater[0])   
        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j] == 1:
                    que.append([i, j])


        turn = 2  
        while que:
            x = len(que)
            for _ in range(x):
                row, col = que.popleft()
                for x, y in dirs:
                    new_row = row + x
                    new_col = col + y
                    if inbound(new_row, new_col) and isWater[new_row][new_col] == 0:
                        isWater[new_row][new_col] = turn
                        que.append([new_row, new_col])
            turn += 1
        
        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                isWater[i][j] -= 1
        return isWater