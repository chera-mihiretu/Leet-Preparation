from typing import *
from collections import defaultdict
from heapq import *
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n = defaultdict(list)
        answer = -1
        for i in range(len(nums)):
            temp = nums[i]
            s = 0
            while temp:
                s += temp % 10
                temp //= 10
            if n[s]:
                answer = max(answer, nums[i] + (-n[s][0]))
            
            heappush(n[s], -nums[i])
        return answer
