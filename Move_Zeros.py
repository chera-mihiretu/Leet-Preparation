from typing import *
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[start] = nums[start],nums[i]
                start += 1        