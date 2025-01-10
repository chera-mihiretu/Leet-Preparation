from typing import *

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        M = max(nums) - min(nums)
        n = len(nums)
        dp = [[0] * (M + 1) for _ in range(2 * M + max(nums) + 2)]
        res = 1
        for i in range(n - 1, -1, -1):
            curr = [0] * (M + 1)
            l = 1
            for diff in range(0, M + 1):
                l = max(l, 1 + dp[nums[i] - diff][diff], 1 + dp[nums[i] + diff][diff])
                curr[diff] = l
                res = max(res, l)
            for diff in range(0, M + 1):
                dp[nums[i]][diff] = max(dp[nums[i]][diff], curr[diff])
        
        return res
    
x = Solution()

print(x.longestSubsequence([5, 10, 8, 20, 10, 20]))