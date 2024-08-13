from typing import *
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        def dfs(choosen, path):
            if len(path) == len(nums):
                answer.add(tuple(path))
            for i in range(len(nums)):
                if not (1 << i) & choosen:
                    path.append(nums[i])
                    dfs(choosen | (1 << i), path)
                    path.pop()
        dfs(0, [])
        return answer
            