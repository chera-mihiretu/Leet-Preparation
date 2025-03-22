from typing import *
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        answer = 1
        inc_count = 1
        dec_count = 1
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                inc_count = 1
            else:
                inc_count += 1

            if nums[i] >= nums[i-1]:
                dec_count = 1
            else:
                dec_count += 1
            answer = max(answer, inc_count, dec_count)
        return answer