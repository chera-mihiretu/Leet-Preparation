from typing import *

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if i + 1 < len(nums) and  nums[i+1] >= nums[i-1]:
                    nums[i] = nums[i+1] if i + 1 < len(nums) else float('inf')
                    break
                elif i + 1 < len(nums):
                    nums[i-1] = nums[i]
                    break
                else:
                    nums[i] = nums[i-1]
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                return False
        return True
        
            