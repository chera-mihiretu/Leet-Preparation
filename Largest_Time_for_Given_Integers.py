from typing import *

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        def possible(nums):

            if nums[0] > 2 or nums[0] == float('-inf'):
                return False
            if nums[0] == 2 and nums[1] > 3:
                return False
            if nums[2] > 5:
                return False
            return True
        def rec(nums, picked):
            if picked == ((1 << 4) - 1):
                
                return nums[::]

            result = [float('-inf')]
            for i in range(4):
                if picked & (1 << i) == 0:
                    nums.append(arr[i])
                    
                    value = rec(nums, picked | (1 << i))
                    
                    if possible(value):

                        result = max(result, value)

                    nums.pop()
            return result
        total = rec([], 0)
        if total[0] == float('-inf'):
            return ''
        return str(total[0]) + str(total[1]) + ':' + str(total[2]) + str(total[3])

                