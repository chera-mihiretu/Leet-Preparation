from typing import *
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        answer = float('inf')
        total = 0
        start = 0
        for i in range(len(nums)):
            total += nums[i]
            while total - nums[start] >= target:
                total -= nums[start]
                start +=1
            if total >= target:
                answer = min(answer, i - start + 1)
        return answer if answer != float('inf') else 0
