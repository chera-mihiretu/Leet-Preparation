from typing import *
class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 2:
            return int(n != 0)
        nums = [0 for i in range(n + 1)]
        nums[1] = nums[2] = 1
        nums[0] = 0
        for i in range(3, len(nums)):
            nums[i] = nums[i - 1] + nums[i - 2] + nums[i - 3]
        
        return nums[n]