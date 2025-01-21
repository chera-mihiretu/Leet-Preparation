from typing import *
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        N = len(grid[0])
        right = [0]
        left = [0]

        for i in range(N):
            right.append(right[-1] + grid[1][i])
        for i in range(N - 1, -1, -1):
            left.append(left[-1] + grid[0][i])
        left = left[::-1]

        answer = float('inf')
        for i in range(N):
            curr = max(right[i], left[i+1])
            answer = min(curr, answer)
        return answer

        

