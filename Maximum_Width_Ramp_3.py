from typing import *

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        answer = 0
        for i in range(len(nums)):
            if stack and nums[stack[-1]] <= nums[i]:
                continue
            stack.append(i)
        
        for i in range(len(nums)-1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                index = stack.pop()
                answer = max(i - index, answer)
        return answer