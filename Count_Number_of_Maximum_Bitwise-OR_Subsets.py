from typing import *

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        ored_val = 0
        answer = 0
        for num in nums:
            ored_val |= num
        def number(index, ored):
            nonlocal answer

            if index == len(nums):
                if ored == ored_val:
                    return 1 
                return 0
            
            return number(index + 1, ored) + number(index + 1, ored | nums[index])
        return number(0,0)


