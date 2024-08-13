from typing import *
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def backtrack(index, path):
            if index == len(nums):
                answer.append(path[:])
                return
            path.append(nums[index])
            backtrack(index + 1, path)
            path.pop()
            backtrack(index + 1, path)
        backtrack(0, [])
        return answer
            

