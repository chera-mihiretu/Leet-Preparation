from typing import *
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        answer = (len(nums) * (len(nums) + 1)) / 2 
        answer -= len(nums)

        non_answer = 0
        h = {}
        for i in range(len(nums)):
            dif = nums[i] - i
            if dif in h:
                answer -= h[dif]
            h[dif] = h.get(dif, 0) + 1

        return int(answer)