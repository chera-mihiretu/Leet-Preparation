from typing import *

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])

        def inbound(row, col):
            return 0 <= row < N and 0 <= col < M
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]

        distance = [[float('inf') for _ in range(M)] for __ in range(N)]
        visited = [[False for _ in range(M)] for __ in range(N)]
        distance[0][0] = 0
        heap = [[0, (0,0)]]

        while heap:
            # print(heap)
            cur_distance, [row, col] = heappop(heap)
            
            if visited[row][col]:
                continue
            visited[row][col] = True

            for x, y in dirs:
                cur_row = x + row
                cur_col = y + col
                
                if inbound(cur_row, cur_col):
                    possible_distance = cur_distance + grid[cur_row][cur_col]
                    if possible_distance < distance[cur_row][cur_col]:
                        distance[cur_row][cur_col] = possible_distance
                        heappush(heap, [possible_distance, (cur_row, cur_col)])
        
        return distance[N-1][M-1]




