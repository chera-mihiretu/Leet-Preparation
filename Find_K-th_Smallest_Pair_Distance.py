from typing import *

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        start = 0
        nums.sort()
        end = nums[-1]
        while start < end:
            mid = start + (end - start) // 2
            left = 0
            count = 0
            # print('mid', mid)
            for i in range(len(nums)):
                while nums[i] - nums[left] > mid:
                    left += 1
                count += i - left 
            # print('count', count)
            if count >= k:
                end = mid
            else:
                start = mid + 1
        return start