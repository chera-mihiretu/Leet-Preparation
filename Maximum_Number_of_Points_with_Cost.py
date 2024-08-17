from typing import * 
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        dp = points[0]
        for row in range(1, len(points)):
            l_max = [0 for _ in range(len(points[0]))]
            r_max = [0 for _ in range(len(points[0]))]
            current = [0 for _ in range(len(points[0]))]


            l_max[0] = dp[0]
            for col in range(1, len(points[0])):
                l_max[col] = max(l_max[col - 1] - 1, dp[col])
            r_max[-1] = dp[-1]
            for col in range(len(points[0]) - 2, -1,  -1):
                r_max[col] = max(r_max[col + 1] - 1, dp[col])
            for col in range(len(points[0])):
                current[col] = max(r_max[col], l_max[col]) + points[row][col]
            dp = current
        return max(dp)



