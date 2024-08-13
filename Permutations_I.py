from typing import *
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        answer = []
        def dfs(choose, path):
            if len(path) == len(nums):
                answer.append(path.copy())
            for i in range(len(nums)):
                if (1 << i) & choose:
                    path.append(nums[i])
                    dfs(path, choose | (1 << i))
                    path.pop()
        return answer