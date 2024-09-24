from typing import *

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        answer = 0
        start= 0
        prev = 0
        if len(nums) == 1:
            return 1
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            numOfEl = i - start 
            prev = diff * numOfEl + prev
            while prev > k:
                prev -= nums[i] - nums[start]
                start += 1
            answer = max(i - start + 1, answer)
        return answer



