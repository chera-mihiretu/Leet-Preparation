from typing import *
from collections import deque
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        que = deque([[0,0]])
        cur_sum = 0
        answer = float('inf')
        for i in range(len(nums)):
            cur_sum += nums[i]
            while que and cur_sum - que[0][0] >= k:
                answer = min(answer, i + 1 - que.popleft()[1])
                
            while que and que[-1][0] >= cur_sum:
                que.pop()
            que.append([cur_sum, i+1])
            
            
        return answer if answer != float('inf') else -1
            
