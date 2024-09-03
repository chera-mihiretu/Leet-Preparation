from typing import *
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        answer = float('-inf')
        start = current = 0
        for i in range(len(nums)):
            current += nums[i]
            if (i - start + 1) > k:
                current -= nums[start]
                start += 1
            if (i - start + 1) == k:
                answer = max(answer, current / k)
        return answer
            