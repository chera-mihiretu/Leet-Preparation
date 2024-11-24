from typing import * 
from math import ceil
class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        n = len(nums)

        def recursion(index, op1, op2):
            if index == n:
                return 0
            nothing = k_red = half = k_red_both = half_both = float('inf')
            
            # correct 
            nothing = nums[index] + recursion(index + 1, op1, op2)

            if nums[index] >= k and op2: 
                # correct 
                k_red = (nums[index] - k) + recursion(index + 1, op1, op2 - 1)
                # correct 
                if op1:
                    k_red_both = ceil((nums[index]- k) // 2) + recursion(index + 1, op1 - 1, op2 - 1)
            # correct
            if op1:
                half = ceil(nums[index] // 2 ) + recursion(index + 1, op1 - 1, op2)


            if op1 and op2 and ceil(nums[index]//2) >= k:
                half_both = (ceil(nums[index]//2) - k) + recursion(index + 1, op1 - 1, op2 - 1)
            return min( nothing, k_red, half, k_red_both,  half_both)
        return recursion(0, op1, op2)

              