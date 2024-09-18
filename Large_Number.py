from typing import *
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        def based(num1, num2):
            if num1+num2 > num2+num1:
                return True
            return False
        for i in range(1, len(nums)):
            while i > 0  and based(nums[i], nums[i-1]):
                nums[i], nums[i-1] =  nums[i-1], nums[i]
                i -= 1
                
            
            
        answer =  "".join(nums)
        start = 0
        while start < len(answer) - 1:
            if answer[start] == "0":
                start +=1
            else:
                break
        return answer[start:]