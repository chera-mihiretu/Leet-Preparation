from typing import *
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        
        answer = nums[0]
        
        dec_count = nums[0]
       

        for i in range(1, len(nums)):
            
            if nums[i] <= nums[i-1]:
                dec_count = nums[i]
               
            else:
                dec_count += nums[i]
                
            answer = max(answer, dec_count)
        return answer