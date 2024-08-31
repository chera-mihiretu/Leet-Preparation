from typing import *
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_map = {}
        for i in range(len(nums)):
            if nums[i] in my_map:
                if i - my_map[nums[i]] <= k:
                    return True
            my_map[nums[i]] = i
        return False