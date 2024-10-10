from typing import *

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        left_max = [0 for i in range(len(nums))]
        left_max[-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            left_max[i] = max(left_max[i + 1], nums[i])
        left, right, answer = 0,0,0
        while right < len(nums):
            if left < len(nums) and nums[left] > left_max[right]:
                left += 1
            answer = max(answer, right - left)
            right += 1
        return answer