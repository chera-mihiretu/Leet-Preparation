from typing import *
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        x = 0
        k = (1 << maximumBit) - 1
        for i in range(len(nums)):
            x ^= nums[i]
        answer = []
        for i in range(len(nums)-1, -1, -1):
            answer.append(k - x)
            x ^= nums[i]
        return answer