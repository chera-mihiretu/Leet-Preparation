from typing import *
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        num_index = [i for i in range(len(nums))]
        num_index.sort(key=lambda x: nums[x])
        min_ind = float('inf')
        answer = 0
        for i in range(len(nums)):
            min_ind = min(min_ind, num_index[i])
            answer = max(num_index[i] - min_ind, answer)
        return answer