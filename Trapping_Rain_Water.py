from typing import *

class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0 for i in range(len(height))]
        right_max = [0 for i in range(len(height))]

        left_max[0] = height[0]
        right_max[-1] = height[-1]
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i-1], height[i])

        for j in range(len(height) -2 , -1, -1):
            right_max[j] = max(right_max[j+1], height[j])
        
        answer = 0
        for i in range(len(height)):
            answer += max(0, min(left_max[i], right_max[i]) - height[i])

        # print(left_max, right_max)
        return answer